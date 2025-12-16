from django.urls import path

from apps.bible_change.users.views.auth.my_page import MyPageAPIView
from apps.bible_change.users.views.auth.signup import SignupAPIView
from apps.bible_change.users.views.auth.withdrawal import WithdrawalApiView
from apps.bible_change.users.views.auth.email_login import EmailLoginAPIView



app_name = "users"

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="signup"),
    path("withdrawal/", WithdrawalApiView.as_view(), name="withdrawal"),
    path("my_page/<str:user_id>/", MyPageAPIView.as_view(), name="my_page"),
    path("email_login/", EmailLoginAPIView.as_view(), name="email_login"),


]
