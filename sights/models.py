from django.db import models
from datetime import timedelta


# Create your models here.
class Sight(models.Model):
    created_by = models.ForeignKey('staff.CustomUser', related_name='sights', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='sights', null=True, blank=True)
    shared = models.BooleanField(default=False)
    timing = models.DurationField(default=timedelta(hours=1))

    @property
    def last_price(self) -> 'Price':
        return self.prices.last()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Price(models.Model):
    sight = models.ForeignKey('Sight', related_name='prices', on_delete=models.CASCADE)
    adult_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    kid_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f'Price: {self.sight.title} | {self.adult_price} | {self.kid_price}'
