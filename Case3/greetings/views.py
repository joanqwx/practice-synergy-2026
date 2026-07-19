"""Представления приложения greetings."""

from django.shortcuts import render

from .forms import UserNameForm


def home(request):
    """Показывает форму и сохраняет корректно введённое имя."""
    greeting = None
    if request.method == "POST":
        form = UserNameForm(request.POST)
        if form.is_valid():
            saved_name = form.save()
            greeting = saved_name.name
            form = UserNameForm()
    else:
        form = UserNameForm()

    return render(request, "home.html", {"form": form, "greeting": greeting})
