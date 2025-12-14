# apps/bible_change/users/serializers/mypage_serializer.py

from rest_framework import serializers
from apps.bible_change.users.models import User


class MyPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "nickname",
            "name",
            "gender",
            "membership",
            "birth_date",
            "phone_number",
            "road_address",
            "detail_address",
            "zip_code",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "email",
            "membership",
            "created_at",
            "updated_at",
        ]
