import pytest
from rest_framework import status
from django.urls import reverse
from apps.bible_change.users.models.user import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestSignupAPIView:

    def test_signup_success(self, api_client):
        url = reverse("users:signup")
        payload = {
            "id": "testuser01",
            "password": "GoodPass12!",
            "password2": "GoodPass12!",
            "name": "홍길동",
            "nickname": "테스트유저",
            "email": "testuser@example.com",
            "gender": "M",
            "level": "ADMIN",
            "membership": "SEEKER",
            "birth_date": "1999-01-01",  # ← 수정
            "phone_number": "01012345678",
        }

        response = api_client.post(url, data=payload, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["message"] == "회원가입 성공~! 관리자의 승인을 기다리세요"

        user_data = response.data["user"]
        assert user_data["email"] == payload["email"]
        assert user_data["nickname"] == payload["nickname"]
        assert str(user_data["birth_date"]) == payload["birth_date"]
        assert user_data["gender"] == payload["gender"]
        assert user_data["phone_number"] == payload["phone_number"]

        assert User.objects.filter(email=payload["email"]).exists()


    def test_signup_password_mismatch_fail(self, api_client):
        url = reverse("users:signup")
        payload = {
            "id": "testuser01",
            "password": "GoodPass12!",
            "password2": "WrongPass9!",   # 틀리게
            "name": "홍길동",
            "nickname": "실패유저",
            "email": "testuser@example.com",
            "gender": "M",
            "level": "ADMIN",
            "membership": "SEEKER",
            "birth_date": "1999,01,01",
            "phone_number": "01012345678",
        }
        response = api_client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not User.objects.filter(email=payload["email"]).exists()


    def test_signup_duplicate_email_fail(self, api_client):
        User.objects.create_user(
            id="dup123@@",
            email="dup@example.com",
            password="GoodPass12!",
            nickname="기존유저",
        )

        url = reverse("users:signup")
        payload = {
            "id": "dup123@@",
            "email": "dup@example.com",
            "password": "GoodPass12!",
            "password2": "GoodPass12!",
            "nickname": "중복유저",
            "birth_date": "2000,01,01",
            "gender": "M",
            "phone_number": "01099998888",
            "membership": "SEEKER",
            "Level": "ADMIN",
        }

        response = api_client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
