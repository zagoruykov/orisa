import logging
from decimal import Decimal
from functools import reduce

import pytest

from trips.models import Trip, Day, DaySight, VehiclesTrips, GuideTrips

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_trip_1_expenses_total(base_trip_1: Trip):
    valid_values = [Decimal('246000'), Decimal('285900'), Decimal('285900')]
    for (day, valid_value) in zip(Day.objects.with_calculations().filter(trip=base_trip_1).all(), valid_values):
        vehicles = day.vehiclestrips_set.all()
        vehicles_price = reduce(lambda acc, curr: acc + curr.price, vehicles, Decimal('0.00'))
        logger.info(vehicles)
        logger.info(vehicles_price)
        guides = day.guidetrips_set.all()
        guides_price = reduce(lambda acc, curr: acc + curr.price, guides, Decimal('0.00'))
        logger.info(guides)
        logger.info(guides_price)
        sights = day.daysight_set.all()
        logger.info(sights)
        logger.info(day.total_adults)
        logger.info(day.total_shared)
        total = vehicles_price + guides_price + day.total_adults + day.total_shared
        assert total == valid_value
    assert Trip.objects.count() == 1
    assert Day.objects.count() == 3
    assert VehiclesTrips.objects.count() == 3
    assert GuideTrips.objects.count() == 3
    assert DaySight.objects.count() == 18
    assert base_trip_1


@pytest.mark.django_db
def test_trip_1_expenses_per_person(base_trip_1: Trip):
    valid_values = [Decimal('6150.00'), Decimal('7147.50'), Decimal('7147.50')]
    for (day, valid_value) in zip(Day.objects.with_calculations().filter(trip=base_trip_1).all(), valid_values):
        vehicles = day.vehiclestrips_set.all()
        vehicles_price = reduce(lambda acc, curr: acc + curr.price, vehicles, Decimal('0.00'))
        logger.info(vehicles)
        logger.info(vehicles_price)
        guides = day.guidetrips_set.all()
        guides_price = reduce(lambda acc, curr: acc + curr.price, guides, Decimal('0.00'))
        logger.info(guides)
        logger.info(guides_price)
        sights = day.daysight_set.all()
        logger.info(sights)
        logger.info(day.total_adults)
        logger.info(day.total_shared)
        per_person = (vehicles_price + guides_price + day.total_adults + day.total_shared) / day.trip.adults
        assert per_person == valid_value

    assert base_trip_1


@pytest.mark.django_db
def test_trip_2_expenses_total(base_trip_2: Trip):
    valid_values = [Decimal('42050')]
    for (day, valid_value) in zip(Day.objects.with_calculations().filter(trip=base_trip_2).all(), valid_values):
        vehicles = day.vehiclestrips_set.all()
        vehicles_price = reduce(lambda acc, curr: acc + curr.price, vehicles, Decimal('0.00'))
        logger.info(vehicles)
        logger.info(vehicles_price)
        guides = day.guidetrips_set.all()
        guides_price = reduce(lambda acc, curr: acc + curr.price, guides, Decimal('0.00'))
        logger.info(guides)
        logger.info(guides_price)
        sights = day.daysight_set.all()
        logger.info(sights)
        logger.info(day.total_adults)
        logger.info(day.total_shared)
        total = vehicles_price + guides_price + day.total_adults + day.total_shared
        assert total == valid_value
    assert Trip.objects.count() == 1
    assert VehiclesTrips.objects.count() == 1
    assert VehiclesTrips.objects.count() == 1
    assert GuideTrips.objects.count() == 1
    assert DaySight.objects.count() == 2
    assert base_trip_2


@pytest.mark.django_db
def test_trip_2_expenses_per_person(base_trip_2: Trip):
    valid_values = [Decimal('6007.14')]
    for (day, valid_value) in zip(Day.objects.with_calculations().filter(trip=base_trip_2).all(), valid_values):
        vehicles = day.vehiclestrips_set.all()
        vehicles_price = reduce(lambda acc, curr: acc + curr.price, vehicles, Decimal('0.00'))
        logger.info(vehicles)
        logger.info(vehicles_price)
        guides = day.guidetrips_set.all()
        guides_price = reduce(lambda acc, curr: acc + curr.price, guides, Decimal('0.00'))
        logger.info(guides)
        logger.info(guides_price)
        sights = day.daysight_set.all()
        logger.info(sights)
        logger.info(day.total_adults)
        logger.info(day.total_shared)
        per_person = (vehicles_price + guides_price + day.total_adults + day.total_shared) / day.trip.adults
        assert round(per_person, 2) == valid_value

    assert base_trip_2


@pytest.mark.django_db
def test_trip_3_expenses_total(base_trip_3):
    valid_values = [Decimal('1902000.00'), Decimal('910000.00'), Decimal('494000.00')]
    for (day, valid_value) in zip(Day.objects.with_calculations().filter(trip=base_trip_3).all(), valid_values):
        vehicles = day.vehiclestrips_set.all()
        vehicles_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, vehicles, Decimal('0.00'))
        logger.info(vehicles)
        logger.info(vehicles_price)
        guides = day.guidetrips_set.all()
        guides_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, guides, Decimal('0.00'))
        logger.info(guides)
        logger.info(guides_price)
        sights = day.daysight_set.all()
        logger.info(sights)
        logger.info(day.total_adults)
        logger.info(day.total_shared)
        total = vehicles_price + guides_price + day.total_adults + day.total_shared
        assert total == valid_value
    assert Trip.objects.count() == 1
    assert Day.objects.count() == 3
    assert VehiclesTrips.objects.count() == 3
    assert GuideTrips.objects.count() == 2
    assert DaySight.objects.count() == 16
    assert base_trip_3


@pytest.mark.django_db
def test_trip_3_expenses_per_person(base_trip_3: Trip):
    valid_values = [Decimal('15850.00'), Decimal('7583.33'), Decimal('4116.67')]
    for (day, valid_value) in zip(Day.objects.with_calculations().filter(trip=base_trip_3).all(), valid_values):
        vehicles = day.vehiclestrips_set.all()
        vehicles_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, vehicles, Decimal('0.00'))
        logger.info(vehicles)
        logger.info(vehicles_price)
        guides = day.guidetrips_set.all()
        guides_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, guides, Decimal('0.00'))
        logger.info(guides)
        logger.info(guides_price)
        sights = day.daysight_set.all()
        logger.info(sights)
        logger.info(day.total_adults)
        logger.info(day.total_shared)
        per_person = (vehicles_price + guides_price + day.total_adults + day.total_shared) / day.trip.adults
        assert round(per_person, 2) == valid_value

    assert base_trip_3
