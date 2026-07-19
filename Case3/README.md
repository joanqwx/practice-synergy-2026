# Case3 — Django-приложение приветствия

Приложение принимает имя через форму, сохраняет его в SQLite и выводит персональное приветствие.

## Запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

После запуска откройте http://127.0.0.1:8000/.

## Проверка

```bash
python manage.py test
```

