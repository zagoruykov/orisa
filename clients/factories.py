import factory

from .models import Client


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    firstName = factory.Faker('first_name')
    lastName = factory.Faker('last_name')
    passport_info = factory.Faker('ssn')
