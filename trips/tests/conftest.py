import datetime
import logging

import pytest

from sights.factories import SightFactory
from staff.factories import VehicleFactory, GuideFactory
from trips.factories import TripFactory, GuideTripsFactory, VehiclesTripsFactory, DayFactory, DaySightFactory

logger = logging.getLogger(__name__)


@pytest.fixture
def base_trip_1():
    ADULTS = 40
    KIDS = 0
    FREE = 0
    EXTRA = 2
    trip = TripFactory.create(
        client__firstName='Vitaliy',
        client__lastName='Zagoruyko',
        adults=ADULTS,
        kids=KIDS,
        free=FREE,
    )
    date1 = datetime.date(2023, 3, 13)
    # Attach new day
    day1 = DayFactory.create(trip=trip, date=date1)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day1, vehicle=VehicleFactory.create(), price=30000, quantity=1)
    # Attach new guide
    GuideTripsFactory.create(day=day1, guide=GuideFactory.create(), price=6000, quantity=1)
    # Attach new sightseeing's
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=True),
                           adult_price=9000,
                           adults_quantity=1,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS + 2,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=600,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=1800,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=1300,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=800,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),

    date2 = datetime.date(2023, 3, 14)
    # Attach new day
    day2 = DayFactory.create(trip=trip, date=date2)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day2, vehicle=VehicleFactory.create(), price=90000, quantity=1)
    # Attach new guide
    GuideTripsFactory.create(day=day2, guide=GuideFactory.create(), price=14000, quantity=1)
    # Attach new sightseeing's
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS + 2,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=350,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=2450,
                           adults_quantity=ADULTS + 2,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=100,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    date3 = datetime.date(2023, 3, 15)
    # Attach new day
    day3 = DayFactory.create(trip=trip, date=date3)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day3, vehicle=VehicleFactory.create(), price=90000, quantity=1)
    # Attach new guide
    GuideTripsFactory.create(day=day3, guide=GuideFactory.create(), price=14000, quantity=1)
    # Attach new sightseeing's
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS + 2,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=350,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=2450,
                           adults_quantity=ADULTS + 2,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=100,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=500,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),

    return trip


@pytest.fixture
def base_trip_2():
    ADULTS = 7
    KIDS = 0
    FREE = 0
    EXTRA = 2
    trip = TripFactory.create(
        client__firstName='Vitaliy',
        client__lastName='Zagoruyko',
        adults=ADULTS,
        kids=KIDS,
        free=FREE,
    )
    date1 = datetime.date(2023, 3, 13)
    # Attach new day
    day1 = DayFactory.create(trip=trip, date=date1)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day1, vehicle=VehicleFactory.create(), price=16000, quantity=1)
    # Attach new guide
    GuideTripsFactory.create(day=day1, guide=GuideFactory.create(), price=7000, quantity=1)
    # Attach new sightseeings
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=True),
                           adult_price=15000,
                           adults_quantity=1,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=450,
                           adults_quantity=ADULTS + EXTRA,
                           kid_price=0,
                           kids_quantity=0),
    return trip


@pytest.fixture
def base_trip_3():
    ADULTS = 120
    KIDS = 0
    FREE = 0
    EXTRA = 0
    trip = TripFactory.create(
        client__firstName='Vitaliy',
        client__lastName='Zagoruyko',
        adults=ADULTS,
        kids=KIDS,
        free=FREE,
    )
    date1 = datetime.date(2023, 3, 13)
    # Attach new day
    day1 = DayFactory.create(trip=trip, date=date1)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day1, vehicle=VehicleFactory.create(), price=45000, quantity=4)
    # Attach new guide
    GuideTripsFactory.create(day=day1, guide=GuideFactory.create(), price=7000, quantity=4)
    # Attach new sightseeings
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=True),
                           adult_price=2500,
                           adults_quantity=4,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=True),
                           adult_price=16000,
                           adults_quantity=1,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=True),
                           adult_price=3000,
                           adults_quantity=8,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=100,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=600,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=6000,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=6000,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day1,
                           sight=SightFactory.create(shared=False),
                           adult_price=1000,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),

    date2 = datetime.date(2023, 3, 14)
    # Attach new day
    day2 = DayFactory.create(trip=trip, date=date2)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day2, vehicle=VehicleFactory.create(), price=45000, quantity=4)
    # Attach new guide
    GuideTripsFactory.create(day=day2, guide=GuideFactory.create(), price=5000, quantity=4)
    # Attach new sightseeings
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=True),
                           adult_price=50000,
                           adults_quantity=1,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=True),
                           adult_price=3000,
                           adults_quantity=8,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=1800,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=2000,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day2,
                           sight=SightFactory.create(shared=False),
                           adult_price=1500,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    date3 = datetime.date(2023, 3, 15)
    # Attach new day
    day3 = DayFactory.create(trip=trip, date=date3)
    # Attach new vehicle
    VehiclesTripsFactory.create(day=day3, vehicle=VehicleFactory.create(), price=35000, quantity=4)
    # Attach new sightseeings
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=True),
                           adult_price=3000,
                           adults_quantity=8,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=1250,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),
    DaySightFactory.create(day=day3,
                           sight=SightFactory.create(shared=False),
                           adult_price=1500,
                           adults_quantity=ADULTS,
                           kid_price=0,
                           kids_quantity=0),

    return trip
