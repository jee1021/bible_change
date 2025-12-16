# apps/bible_change/bible_relay/models/relay_comment.py
from django.db import models
from django.conf import settings
from apps.bible_change.bible_relay.models.relay import Relay


class RelayComment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="relay_comments",
    )
    relay = models.ForeignKey(
        Relay,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
