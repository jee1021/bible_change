from django.contrib.auth import authenticate
from rest_framework import serializers
from apps.bible_change.users.models.user import User

class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self,attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password :
            raise serializers.ValidationError("이메일과 비밀번호는 필수입니다.")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("존재하지 않는 이메일입니다.")
        if not user.check_password(password):
            raise serializers.ValidationError("비밀번호가 올바르지 않습니다.")


        attrs ["user"] = user
        return attrs

