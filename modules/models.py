from django.db import models

from config import settings
from users.models import User

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Educational(models.Model):
    number = models.IntegerField(default=0, verbose_name='порядковый номер')
    name = models.CharField(max_length=30, verbose_name='название модуля')
    description = models.TextField(**NULLABLE, verbose_name='описание модуля')
    amount = models.IntegerField(default=70000, verbose_name='цена модуля')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE) # автоматически удаляет строку из зависимой таблицы

    def __str__(self):
        return f'{self.number} {self.name}'

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='название модуля')
    description = models.TextField(**NULLABLE, verbose_name='описание модуля')
    amount = models.IntegerField(default=70000, verbose_name='цена модуля')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    educational = models.ForeignKey(Educational, on_delete=models.CASCADE, verbose_name='модуль') # автоматически удаляет строку из зависимой таблицы

    def __str__(self):
        return f'{self.name} {self.amount}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
