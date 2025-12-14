from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny  # 회원가입은 인증 필요 없음
from apps.bible_change.users.models.user import User
from apps.bible_change.users.serializers.auth.signup import SignupSerializer
_=User
class SignupAPIView(APIView):
    permission_classes = [AllowAny]  # 회원가입은 로그인 필요 없음
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "회원가입 성공~! 관리자의 승인을 기다리세요",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "nickname": user.nickname,
                    "birth_date": user.birth_date,
                    "gender": user.gender,
                    "phone_number": user.phone_number,
                    "level": user.level  # 변수명 통일 (Level → level)
                }
            },
            status=status.HTTP_201_CREATED
        )
