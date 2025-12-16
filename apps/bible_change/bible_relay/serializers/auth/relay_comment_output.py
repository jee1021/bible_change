from rest_framework import serializers
from apps.bible_change.bible_relay.models.relay import Relay




class RelayCommentOutputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = RelayComment
        fields = [
            "id",
            "username",
            "content",
            "created_at",
        ]