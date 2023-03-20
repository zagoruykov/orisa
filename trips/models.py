import locale
from functools import reduce
from decimal import Decimal
from django.db import models
from django.db.models.functions import TruncDate, TruncTime

from .managers import DayManager
from .services import create_program_docx


class GuideTrips(models.Model):
    day = models.ForeignKey('trips.Day', on_delete=models.CASCADE)
    guide = models.ForeignKey('staff.Guide', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()


class VehiclesTrips(models.Model):
    day = models.ForeignKey('trips.Day', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('staff.Vehicle', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()


# Create your models here.
class Trip(models.Model):
    client = models.ForeignKey('clients.Client', related_name='trips', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    adults = models.PositiveSmallIntegerField(default=0)
    kids = models.PositiveSmallIntegerField(default=0)
    free = models.PositiveSmallIntegerField(default=0)
    commission = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    profit = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    def group(self):
        return self.adults + self.kids + self.free

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for day in self.days.all():
            for day_sight in day.daysight_set.all():
                day_sight.save()
        super().save(*args, **kwargs)

    def __reduce_values(self, acc: dict, curr: 'Day'):
        adult_price = curr.sight.last_price.adult_price if curr.sight.last_price else 0
        kids_price = curr.sight.last_price.kids_price if curr.sight.last_price else 0
        if curr.sight.shared:
            acc['total_shared'] += adult_price
        else:
            acc['total_adults'] += adult_price * (self.adults + self.free)
            acc['total_kids'] += kids_price * self.kids
        return acc

    def calculate_total(self):
        total = reduce(self.__reduce_values, self.day_set.all(),
                       {'total_adults': 0, 'total_kids': 0, 'total_shared': 0})
        # price_for_adults = self.adults * reduce(lambda acc, curr: acc + curr.sight.last_price.adult_price,
        #                                         self.day_set.all(), 0)
        # price_for_free = self.free * reduce(lambda acc, curr: acc + curr.sight.last_price.adult_price,
        #                                     self.day_set.all(), 0)
        # price_for_vehicle = self.vehicle.price
        # total = price_for_kids + price_for_adults + price_for_free + price_for_vehicle
        guides_price = reduce(lambda acc, curr: acc + curr.price, self.guidetrips_set.all(), 0)
        vehicles_price = self.vehicle.price
        return total['total_adults'] + total['total_kids'] + total['total_shared'] + guides_price + vehicles_price

    def calculate_per_person(self):
        return round(self.calculate_total() / (self.adults + self.kids + self.free), 2)

    def generate_program(self):
        create_program_docx(self)

    def dump_to_to_docx(self):
        return self.day_set.annotate(day=TruncDate('datetime_start')).annotate(time=TruncTime('datetime_start')).values(
            'sight__title', 'day', 'time')


class Day(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name='days')
    date = models.DateField()
    vehicles = models.ManyToManyField('staff.Vehicle', through='trips.VehiclesTrips')
    guides = models.ManyToManyField('staff.Guide', through='trips.GuideTrips')
    sights = models.ManyToManyField('sights.Sight', through='trips.DaySight')
    objects = DayManager()

    def __str__(self):
        return f'{self.trip.title} - {self.date}'

    def __set_locale(self):
        locale.setlocale(locale.LC_TIME, 'ru_RU')

    def datetime_to_human(self):
        format_str = '%d %B'
        return self.datetime_start.strftime(format_str), self.datetime_end.strftime(format_str)


class DaySight(models.Model):
    day = models.ForeignKey('trips.Day', on_delete=models.CASCADE)
    sight = models.ForeignKey('sights.Sight', on_delete=models.CASCADE)
    adult_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    adults_quantity = models.PositiveSmallIntegerField(default=0)
    kid_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    kids_quantity = models.PositiveSmallIntegerField(default=0)
    start_at = models.TimeField(blank=True, null=True)
    end_at = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Sight'

    def __str__(self):
        return f'{self.sight.title}'

    def save(self, *args, **kwargs):
        if self.adult_price == Decimal('0.00'):
            self.adult_price = self.sight.last_price.adult_price
        if self.adults_quantity == 0:
            self.adults_quantity = self.day.trip.adults
        if self.kid_price == Decimal('0.00'):
            self.kid_price = self.sight.last_price.kid_price
        if self.kids_quantity == 0:
            self.kids_quantity = self.day.trip.kids

        super().save(*args, **kwargs)
