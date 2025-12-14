from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.bible_change.users.manager.user_manager import CustomUserManager
import uuid


def generate_user_id():
    return uuid.uuid4().hex[:13]


def default_birth_date():
    return date(1989, 12, 31)


class User(AbstractBaseUser, PermissionsMixin):

    class Level(models.TextChoices):
        ADMIN = ("ADMIN", "바이블체인지 관리자")
        MENTOR = ("MENTOR", "멘토 / 양육erial자")
        MEMBER = ("MEMBER", "일반 멤버")
        VISITOR = ("VISITOR", "새가족 / 방문자")

    class Membership(models.TextChoices):
        SEEKER = ("SEEKER", "말씀 탐색자")
        ROOTED = ("ROOTED", "말씀에 뿌리내린 자")
        GROWING = ("GROWING", "성장하는 자")
        FRUITFUL = ("FRUITFUL", "열매 맺는 자")
        LIGHT = ("LIGHT", "빛을 비추는 자")

    class Gender(models.TextChoices):
        MALE = ("M", "남성")
        FEMALE = ("F", "여성")

    id = models.CharField(
        max_length=13,
        primary_key=True,
        default=generate_user_id,  # ✅ lambda 제거
        editable=False
    )

    password = models.CharField(max_length=13, help_text="비밀번호(7~13자)")
    password2 = models.CharField(max_length=13, blank=True, null=True)

    name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)

    gender = models.CharField(max_length=8, choices=Gender.choices, default=Gender.MALE)
    level = models.CharField(max_length=8, choices=Level.choices, default="ADMIN")
    membership = models.CharField(max_length=10, choices=Membership.choices, default="SEEKER")

    birth_date = models.DateField(default=default_birth_date)
    phone_number = models.CharField(max_length=11, unique=True)
    road_address = models.CharField(max_length=255, blank=True, null=True)
    detail_address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - ({self.get_level_display()})"

    def save(self, *args, **kwargs):
        if self.level in {self.Level.ADMIN, self.Level.MENTOR}:
            self.is_approved = True
        super().save(*args, **kwargs)

    REQUIRED_FIELDS = ["name"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()
