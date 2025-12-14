from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from apps.bible_change.users.models.user import User
from apps.bible_change.users.serializers.auth.email_login import EmailLoginSerializer


class EmailLoginAPIView(APIView):

    def post(self, request):
        serializer = EmailLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        # 이메일 존재 검사
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"errors": "존재하지 않는 이메일입니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 비밀번호 인증
        authenticated_user = authenticate(username=email, password=password)
        if authenticated_user is None:
            return Response(
                {"errors": "비밀번호가 올바르지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔥 테스트 요구: email 필드 포함해야 함
        return Response(
            {
                "message": "로그인 성공",
                "email": authenticated_user.email
            },
            status=status.HTTP_200_OK
        )
