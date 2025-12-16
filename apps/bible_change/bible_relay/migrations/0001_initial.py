from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BibleRelayComment',
            fields=[

                (
                    'book',
                    models.CharField(
                        max_length=50,
                        verbose_name='성경 권'
                    )
                ),
                (
                    'chapter',
                    models.PositiveIntegerField(
                        verbose_name='장'
                    )
                ),
                (
                    'verse',
                    models.PositiveIntegerField(
                        verbose_name='절'
                    )
                ),
                (
                    'content',
                    models.TextField(
                        verbose_name='릴레이 댓글 내용'
                    )
                ),
                (
                    'is_completed',
                    models.BooleanField(
                        default=False,
                        verbose_name='릴레이 완료 여부'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='작성일'
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name='수정일'
                    )
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='bible_relay_comments',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='작성자'
                    )
                ),
            ],
            options={
                'verbose_name': '성경 릴레이 댓글',
                'verbose_name_plural': '성경 릴레이 댓글들',
                'ordering': ['-created_at'],
            },
        ),
    ]
