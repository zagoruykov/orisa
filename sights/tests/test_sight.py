import pytest

from sights.factories import SightFactory


@pytest.mark.django_db
def test_create_sight():
    sight = SightFactory.create()
    assert sight
