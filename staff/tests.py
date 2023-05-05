import pytest

from .factories import CustomUserFactory


@pytest.mark.django_db
def test_create_user():
    user = CustomUserFactory.create()
    assert user
