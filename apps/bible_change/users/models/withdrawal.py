from django.conf import settings
from django.db import models

class Withdrawal(models.Model):

    class Reason(models.TextChoices):
        HABIT_DIFFICULTY = ("HABIT_DIFFICULTY", "말씀/독서 습관 유지 어려움")
        LACK_OF_CONTENT = ("LACK_OF_CONTENT", "콘텐츠 부족")
        UX_ISSUE = ("UX_ISSUE", "앱 사용성 불편")
        DEVICE_ISSUE = ("DEVICE_ISSUE", "기기/환경 문제")
        OTHER_APP = ("OTHER_APP", "다른 앱 사용")
        DUPLICATE = ("DUPLICATE", "중복 계정")
        PRIVACY = ("PRIVACY", "개인 정보 삭제 요청")
        OTHER = ("OTHER", "기타")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="withdrawals",
        null=True,
        blank=True,
        help_text="탈퇴한 사용자",
    )

    reason = models.CharField(
        max_length=30,
        choices=Reason.choices,
        help_text="탈퇴 사유",
    )

    detail = models.TextField(
        null=True,
        blank=True,
        help_text="추가 입력 사유 (선택)",
    )

    withdrawn_at = models.DateTimeField(
        auto_now_add=True,
        help_text="탈퇴 시각",
    )

    def __str__(self):
        return f"{self.user}-{self.get_reason_display()}"
