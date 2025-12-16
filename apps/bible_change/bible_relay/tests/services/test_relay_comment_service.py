import pytest

from apps.bible_change.bible_relay.services.relay_comment_service import (
    RelayCommentService,
)
from apps.bible_change.bible_relay.models import RelayComment


@pytest.mark.django_db
class TestRelayCommentService:

    def test_create_comment_success(self, user, relay):
        # given
        content = "이 말씀 너무 은혜돼요"

        # when
        comment = RelayCommentService.create_comment(
            user=user,
            relay=relay,
            content=content,
        )

        # then
        assert isinstance(comment, RelayComment)
        assert comment.user == user
        assert comment.relay == relay
        assert comment.content == content
        assert RelayComment.objects.count() == 1
