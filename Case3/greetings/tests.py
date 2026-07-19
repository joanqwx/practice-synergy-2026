"""Тесты приложения greetings."""

from django.test import TestCase
from django.urls import reverse

from .models import UserName


class HomeViewTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("greetings:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ваше имя")

    def test_valid_name_is_saved_and_greeted(self):
        response = self.client.post(reverse("greetings:home"), {"name": "Анна"})
        self.assertEqual(UserName.objects.count(), 1)
        self.assertContains(response, "Здравствуйте, Анна!")

    def test_empty_name_shows_validation_error(self):
        response = self.client.post(reverse("greetings:home"), {"name": "   "})
        self.assertEqual(UserName.objects.count(), 0)
        self.assertContains(response, "Пожалуйста, введите имя.")

