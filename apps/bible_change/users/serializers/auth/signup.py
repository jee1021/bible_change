from rest_framework import serializers
from apps.bible_change.users.models.user import User


class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "password",
            "password2",
            "name",
            "nickname",
            "email",
            "gender",
            "level",
            "membership",
            "birth_date",
            "phone_number",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "비밀번호가 일치하지 않습니다."}
            )
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")

        user = User(**validated_data)
        user.set_password(password)
        user.password2 = password2  # 모델 필드이므로 저장은 해야 함
        user.save()
        return user
