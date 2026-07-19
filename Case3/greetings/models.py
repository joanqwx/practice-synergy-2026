"""Модели данных приложения greetings."""

from django.db import models


class UserName(models.Model):
    """Сохранённое имя пользователя."""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

