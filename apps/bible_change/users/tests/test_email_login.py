import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.mark.django_db
class TestEmailLoginAPI:

    def setup_method(self):
        self.Client = APIClient()
        self.url = reverse("users:email_login")

        self.user = User.objects.create(
            email="lovbe12@example.com",
            password="lovber123!!",
            password2="lovber123!!",
            name="홍길준",
            nickname="tester",
            phone_number="01012345678",
        )
        # 🔥 테스트 비밀번호와 반드시 동일하게 셋트해야 함
        self.user.set_password("lovber123!!")
        self.user.save()

    def test_email_login_success(self):
        response = self.Client.post(self.url, {
            "email": "lovbe12@example.com",
            "password": "lovber123!!"
        })
        assert response.status_code == 200
        assert response.data["message"] == "로그인 성공"
        assert response.data["email"] == "lovbe12@example.com"

    def test_email_wrong_password(self):
        response = self.Client.post(self.url, {
            "email": "lovbe12@example.com",
            "password": "wrong"
        })
        assert response.status_code == 400
        assert "비밀번호가 올바르지 않습니다" in str(response.data["errors"])

    def test_email_login_not_exist(self):
        response = self.Client.post(self.url, {
            "email": "npo@example.com",
            "password": "124"
        })
        assert response.status_code == 400
        assert "존재하지 않는 이메일입니다." in str(response.data["errors"])
