import factory

from .models import CustomUser, Guide, Vehicle


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Sequence(lambda n: f'test{n}@test.ru')
    password = factory.Sequence(lambda n: f'test{n}@test.ru')


class GuideFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Guide

    firstName = factory.Faker('first_name')
    lastName = factory.Faker('last_name')


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    title = factory.Faker('name')
    capacity = factory.Faker('pyint')
    type = factory.Faker('name')
