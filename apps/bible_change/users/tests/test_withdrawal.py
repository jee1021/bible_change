import pytest
import uuid
from django.urls import reverse
from rest_framework.test import APIClient
from apps.bible_change.users.models.withdrawal import Withdrawal


@pytest.mark.django_db
class TestWithdrawalAPI:

    def setup_method(self):
        self.Client = APIClient()

    # ------------------------------
    # 1) 성공 테스트
    # ------------------------------
    def test_withdrawal_success(self, django_user_model):
        user = django_user_model.objects.create_user(
            id=uuid.uuid4(),
            email="atesr@example.com",
            password="test1234"
        )
        self.Client.force_authenticate(user=user)

        url = reverse("users:withdrawal")
        data = {
            "reason": "OTHER",
            "detail": "테스트 탈퇴"
        }

        response = self.Client.post(url, data, format="json")

        assert response.status_code == 201
        assert response.data["message"] == "탈퇴가 성공적으로 처리되었습니다."
        assert Withdrawal.objects.count() == 1

        user.refresh_from_db()
        assert user.is_active is False

    # ------------------------------
    # 2) reason 누락 → serializer.is_valid 실패
    # ------------------------------
    def test_withdrawal_no_reason_error(self, django_user_model):
        user = django_user_model.objects.create_user(
            id=uuid.uuid4(),
            email="test12345@example.com",
            password="password1212"
        )
        self.Client.force_authenticate(user=user)

        url = reverse("users:withdrawal")

        response = self.Client.post(url, {}, format="json")

        assert response.status_code == 400

        # top-level message
        assert "message" in response.data
        assert response.data["message"] == "탈퇴 처리 중 사용자 비활성화에 실패했습니다."

        # errors 구조 확인
        assert "errors" in response.data
        assert "message" in response.data["errors"]
        assert "fields" in response.data["errors"]
        assert "reason" in response.data["errors"]["fields"]
        assert "This field is required." in str(response.data["errors"]["fields"]["reason"])

    # ------------------------------
    # 3) reason만 있어도 탈퇴 성공 → user 비활성화
    # ------------------------------
    def test_user_inactive_after_withdrawal(self, django_user_model):
        user = django_user_model.objects.create_user(
            id=uuid.uuid4(),
            email="test@a.com",
            password="pw1234",
        )
        self.Client.force_authenticate(user=user)

        url = reverse("users:withdrawal")
        data = {
            "reason": "PRIVACY",
        }

        self.Client.post(url, data, format="json")

        user.refresh_from_db()
        assert user.is_active is False
