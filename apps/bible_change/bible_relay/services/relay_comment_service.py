# services/relay_comment_service.py

from apps.bible_change.bible_relay.models.relay_comment import RelayComment

class RelayCommentService:
    @staticmethod
    def create_comment(*, user, relay, content):
        comment = RelayComment.objects.create(
            user=user,
            relay=relay,
            content=content,
        )

        return comment
