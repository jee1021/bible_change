from rest_framework import serializers
from apps.bible_change.bible_relay.models.relay import Relay

class RelayCommentInputSerializer(serializers.Serializer):
    verse = serializers.CharField()
    c