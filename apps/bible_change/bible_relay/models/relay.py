from django.db import models
from django.conf import settings



class Relay(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bible_relay_comments",
        verbose_name="바이블 성경댓글 작성자"
    )

    bible_book = models.CharField(
        max_length=3000,
        verbose_name="성경책"
    )
    chapter = models.PositiveIntegerField(
        verbose_name="장"
    )

    verse = models.PositiveIntegerField(
        verbose_name="절"
    )

    content = models.TextField(
        verbose_name="릴레이 댓글 내용"
    )

    is_completed = models.BooleanField(
        default=False,
        verbose_name="릴레이 완료 여부"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="작성일"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="수정일"
    )

    class Meta:
        verbose_name = "성경릴래이댓글"
        verbose_name_plural = "성경릴레이 댓글들"

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} | {self.bible_book} {self.chapter}:{self.verse}"

