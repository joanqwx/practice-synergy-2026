"""Регистрация моделей в панели администратора."""

from django.contrib import admin

from .models import UserName


@admin.register(UserName)
class UserNameAdmin(admin.ModelAdmin):
    """Настройка отображения имён в административной панели."""

    list_display = ("id", "name")
    search_fields = ("name",)

