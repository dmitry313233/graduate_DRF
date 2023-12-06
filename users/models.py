from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='имя')
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.IntegerField(**NULLABLE, verbose_name='номер телефона')
    email = models.EmailField(unique=True, **NULLABLE, verbose_name='почтовый адрес')
    avatar = models.ImageField(upload_to='', **NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
