import pytest
from django.contrib.auth import get_user_model

from apps.bible_change.bible_relay.models.relay import Relay

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        id="test-user-1",
        email="test@example.com",
        password="testpassword123",
    )


@pytest.fixture
def relay(db, user):
    return Relay.objects.create(
        user=user,
        bible_book="창세기",
        chapter=1,
        verse=1,
        content="태초에 하나님이 천지를 창조하시니라",
    )
