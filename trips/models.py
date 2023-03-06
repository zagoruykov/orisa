import locale
from functools import reduce

from django.db import models
from django.db.models.functions import TruncDate, TruncTime

from .services import create_program_docx


class GuideTrips(models.Model):
    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE)
    guide = models.ForeignKey('staff.Guide', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField()


# Create your models here.
class Trip(models.Model):
    client = models.ForeignKey('clients.Client', related_name='trips', on_delete=models.CASCADE)
    guide = models.ManyToManyField('staff.Guide', through='trips.GuideTrips')
    vehicle = models.ForeignKey('staff.Vehicle', related_name='trips', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    adults = models.PositiveSmallIntegerField(default=0)
    kids = models.PositiveSmallIntegerField(default=0)
    free = models.PositiveSmallIntegerField(default=0)
    commission = models.DecimalField(max_digits=15, decimal_places=2)
    profit = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title

    def group(self):
        return self.free + self.kids + self.adults

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
    sights = models.ManyToManyField('sights.Sight', through='trips.DaySight')

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
    extra = models.PositiveSmallIntegerField(default=0)
    start_at = models.TimeField(blank=True, null=True)
    end_at = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Sight'

    def __str__(self):
        return self.sight.title
