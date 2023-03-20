import datetime

import factory
from django.db.models.signals import post_save

from staff.factories import CustomUserFactory
from .models import Sight, Price


class PriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Price

    sight = factory.SubFactory('sights.factories.SightFactory')
    adult_price = factory.Faker('pyint', max_value=1000)
    kids_price = factory.Faker('pyint', max_value=1000)


@factory.django.mute_signals(post_save)
class SightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sight

    created_by = factory.SubFactory(CustomUserFactory)
    title = factory.Faker('name')
    description = factory.Faker('name')
    address = factory.Faker('address')
    contact_phone = factory.Faker('phone_number')
    shared = factory.Faker('pybool')
    timing = factory.LazyFunction(lambda: datetime.timedelta(hours=1))

    @factory.post_generation
    def prices(self: Sight, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for price in extracted:
                self.prices.add(price)
