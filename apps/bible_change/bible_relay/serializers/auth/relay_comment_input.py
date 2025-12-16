from rest_framework import serializers
from apps.bible_change.bible_relay.models.relay import Relay


class RelayCommentInputSerializer(serializers.Serializer):
    verse = serializers.CharField()
    chapter = serializers.CharField()
    content = serializers.CharField()

    def validate(self, attrs):
        verse = attrs["verse"]
        chapter = attrs["chapter"]

        relay = Relay.objects.filter(verse=verse).first()
        if not relay:
            raise serializers.ValidationError(
                "해당 구절의 성경 릴레이가 존재하지 않습니다."
            )

        if not relay.is_ongoing():
            raise serializers.ValidationError(
                "현재 진행 중인 성경 릴레이가 아닙니다."
            )

        if not relay.check_chapter(chapter):
            raise serializers.ValidationError(
                "현재 진행 중인 장이 아닙니다."
            )

        # service에서 쓰기 위해 주입
        attrs["relay"] = relay
        return attrs
