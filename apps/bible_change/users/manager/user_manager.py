from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom User Manager
    User 모델에 맞춰 create_user, create_superuser 구현
    """

    def create_user(self, id, email, password=None, **extra_fields):
        """
        일반 유저 생성
        """
        if not id:
            raise ValueError("Users must have an id")
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            id=id,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, email, password=None, **extra_fields):
        """
        관리자(슈퍼유저) 생성
        """
        extra_fields.setdefault('level', 'ADMIN')
        extra_fields.setdefault('is_approved', True)

        if extra_fields.get('level') != 'ADMIN':
            raise ValueError('Superuser must have level=ADMIN.')

        return self.create_user(id, email, password, **extra_fields)
