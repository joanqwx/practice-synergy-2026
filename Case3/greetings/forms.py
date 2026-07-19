"""Формы приложения greetings."""

from django import forms

from .models import UserName


class UserNameForm(forms.ModelForm):
    """Форма для ввода имени пользователя."""

    class Meta:
        model = UserName
        fields = ("name",)
        labels = {"name": "Ваше имя"}
        error_messages = {
            "name": {
                "required": "Пожалуйста, введите имя.",
            }
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите имя",
                    "autocomplete": "name",
                    "autofocus": True,
                }
            )
        }

    def clean_name(self) -> str:
        """Не допускает пробельное или пустое имя."""
        name = self.cleaned_data["name"].strip()
        if not name:
            raise forms.ValidationError("Пожалуйста, введите имя.")
        return name
