import factory
from django.db.models.signals import post_save

from clients.factories import ClientFactory
from staff.factories import GuideFactory
from .models import Trip, Day, GuideTrips, DaySight, VehiclesTrips


class VehiclesTripsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VehiclesTrips

    day = factory.SubFactory('trips.factories.DayFactory')
    vehicle = factory.SubFactory('staff.factories.VehicleFactory')
    price = factory.Faker('pyint', max_value=10000)
    quantity = factory.Faker('pyint', max_value=10)


@factory.django.mute_signals(post_save)
class GuideTripsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GuideTrips

    day = factory.SubFactory('trips.factories.DayFactory')
    guide = factory.SubFactory(GuideFactory)
    price = factory.Faker('pyint', max_value=10000)
    quantity = factory.Faker('pyint', max_value=10)


@factory.django.mute_signals(post_save)
class DayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day

    trip = factory.SubFactory('trips.factories.TripFactory')
    date = factory.Faker('date_this_month')
    # vehicles = factory.SubFactory('trips.factories.VehiclesTripsFactory')
    # guides = factory.SubFactory('trips.factories.GuideTripsFactory')
    sights = factory.RelatedFactory('trips.factories.DaySightFactory', factory_related_name='day')

    @factory.post_generation
    def sights(self: Day, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for sight in extracted:
                self.daysight_set.add(sight)

    @factory.post_generation
    def vehicles(self: Day, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for vehicle in extracted:
                self.vehiclestrips_set.add(vehicle)

    # @factory.post_generation
    # def trip(self: Day, create, extracted, **kwargs):
    #     if not create:
    #         if extracted:
    #             self.trip = extracted


class DaySightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DaySight

    day = factory.SubFactory('trips.factories.DayFactory')
    sight = factory.SubFactory('sights.factories.SightFactory')
    adult_price = factory.Faker('pyint', max_value=10000)
    adults_quantity = factory.Faker('pyint', max_value=10)
    kid_price = factory.Faker('pyint', max_value=10000)
    kids_quantity = factory.Faker('pyint', max_value=10)
    start_at = factory.Faker('time_object')
    end_at = factory.Faker('time_object')


@factory.django.mute_signals(post_save)
class TripFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Trip

    client = factory.SubFactory(ClientFactory)
    title = factory.Faker('name')
    description = factory.Faker('name')
    adults = factory.Faker('pyint', max_value=10)
    kids = factory.Faker('pyint', max_value=10)
    free = factory.Faker('pyint', max_value=10)
    commission = factory.Faker('pyfloat', positive=True, max_value=10, right_digits=2)
    profit = factory.Faker('pyfloat', positive=True, max_value=30, right_digits=2)

    @factory.post_generation
    def guides(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for guide in extracted:
                self.guidetrips_set.add(guide)

    @factory.post_generation
    def vehicles(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for vehicle in extracted:
                self.vehiclestrips_set.add(vehicle)

    @factory.post_generation
    def days(self: Trip, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for day in extracted:
                self.days.add(day)
