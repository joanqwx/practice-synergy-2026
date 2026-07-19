"""Точка входа для программы работы с датой рождения."""

from datetime import date

from functions import calculate_age, get_day_of_week, is_leap_year, read_birth_date
from digits import print_large_date


def main() -> None:
    """Запрашивает дату рождения и выводит рассчитанную информацию."""
    print("Программа анализа даты рождения")
    print("Введите дату рождения по частям.")

    birth_date = read_birth_date()
    today = date.today()
    age = calculate_age(birth_date, today)
    weekday = get_day_of_week(birth_date)
    leap_text = "високосный" if is_leap_year(birth_date.year) else "невисокосный"

    print("\nРезультат:")
    print(f"Дата рождения: {birth_date.strftime('%d.%m.%Y')}")
    print(f"День недели: {weekday}")
    print(f"Год рождения {birth_date.year} — {leap_text}.")
    print(f"Возраст: {age} лет.")
    print("\nДата рождения большими цифрами:")
    print_large_date(birth_date)


if __name__ == "__main__":
    main()

