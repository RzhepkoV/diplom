from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    short = models.CharField('Сокращенная ссылка', max_length=30)
    long = models.TextField('Длинная ссылка')

    def __str__(self):
        return f'Ссылка {self.short} пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
