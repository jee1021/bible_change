# apps/bible_change/users/views/mypage_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.bible_change.users.models import User
from apps.bible_change.users.serializers.auth.my_page import MyPageSerializer


class MyPageAPIView(APIView):
    """
    GET  : 마이페이지 조회
    PATCH: 마이페이지 수정
    """

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    # -----------------------------
    # GET: 조회
    # -----------------------------
    def get(self, request, user_id: str):
        user = self.get_user(user_id)
        if user is None:
            return Response({
                "message": "존재하지 않는 사용자입니다.",
                "detail": f"user_id '{user_id}' not found",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = MyPageSerializer(user)
        return Response({
            "message": "마이페이지 조회 성공",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # -----------------------------
    # PATCH: 수정
    # -----------------------------
    def patch(self, request, user_id: str):
        user = self.get_user(user_id)
        if user is None:
            return Response({
                "message": "존재하지 않는 사용자입니다.",
                "detail": f"user_id '{user_id}' not found",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = MyPageSerializer(
            user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "마이페이지 수정 성공",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
