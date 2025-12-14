import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from apps.bible_change.users.models import User


@pytest.mark.django_db
class TestMyPageAPI:


    def setup_method(self):
        self.client = APIClient()   # 🔥 DRF용 클라이언트 사용
        self.user = User.objects.create(
            password="1234567",
            nickname="tester",
            email="test@example.com",
            gender="M",
            membership="SEEKER",
            birth_date="1990-01-01",
            phone_number="01012341234",
        )

    # -------------------------
    # 마이페이지 수정 성공
    # -------------------------
    def test_myp_age_update_success(self):
        url = reverse("users:my_page", args=[self.user.id])
        data = {
            "nickname": "newnick",
            "road_address": "서울특별시 강남구",
        }

        response = self.client.patch(url, data, format="json")

        assert response.status_code == 200
        assert response.data["message"] == "마이페이지 수정 성공"
        assert response.data["data"]["nickname"] == "newnick"

    # -------------------------
    # 마이페이지 수정 → 유저 없음
    # -------------------------
    def test_myp_age_update_user_not_found(self):
        url = reverse("users:my_page", args=["invalid_user"])
        data = {"nickname": "test"}

        response = self.client.patch(url, data, format="json")

        assert response.status_code == 404
        assert response.data["message"] == "존재하지 않는 사용자입니다."
