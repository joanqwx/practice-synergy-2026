"""Функции для проверки и обработки даты рождения."""

from datetime import date


WEEKDAYS_RU = (
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
)


def is_leap_year(year: int) -> bool:
    """Возвращает True, если год является високосным по правилам календаря."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_day_of_week(birth_date: date) -> str:
    """Определяет название дня недели для переданной даты."""
    return WEEKDAYS_RU[birth_date.weekday()]


def calculate_age(birth_date: date, current_date: date | None = None) -> int:
    """Вычисляет полный возраст человека на указанную дату."""
    if current_date is None:
        current_date = date.today()

    age = current_date.year - birth_date.year
    has_not_had_birthday = (current_date.month, current_date.day) < (
        birth_date.month,
        birth_date.day,
    )
    return age - int(has_not_had_birthday)


def read_integer(prompt: str, minimum: int, maximum: int) -> int:
    """Считывает целое число из заданного диапазона с повторной попыткой."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Ошибка: число должно быть в диапазоне от {minimum} до {maximum}.")


def read_birth_date() -> date:
    """Запрашивает день, месяц и год и возвращает корректную дату рождения."""
    current_year = date.today().year

    while True:
        day = read_integer("День рождения: ", 1, 31)
        month = read_integer("Месяц рождения: ", 1, 12)
        year = read_integer("Год рождения: ", 1900, current_year)

        try:
            entered_date = date(year, month, day)
        except ValueError:
            print("Ошибка: такой даты не существует. Повторите ввод всех значений.")
            continue

        if entered_date > date.today():
            print("Ошибка: дата рождения не может быть в будущем.")
            continue

        return entered_date

