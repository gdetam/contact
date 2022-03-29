from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager

SEX_TYPES = (
             (0, 'Male'),
             (1, 'Female'),
)


class CustomUser(AbstractUser):
    """class CustomUser create structure object user."""

    class Meta:
        verbose_name = 'Contact user'
        verbose_name_plural = 'Contact user'
        ordering = ['id']

    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/',
                               verbose_name='Аватар', default='logo_profile.png')
    sex = models.IntegerField(choices=SEX_TYPES, default=0, verbose_name='Пол')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField(max_length=150, unique=True,
                              verbose_name='Электронная почта')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
