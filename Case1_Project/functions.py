from datetime import datetime
import calendar
from digits import DIGITS
def get_birth_date():
    while True:
        try:
            d=int(input("Введите день рождения: "))
            m=int(input("Введите месяц рождения: "))
            y=int(input("Введите год рождения: "))
            return datetime(y,m,d)
        except ValueError:
            print("Некорректная дата! Попробуйте снова.")
def get_weekday(dt):
    days=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
    return days[dt.weekday()]
def is_leap(year):
    return calendar.isleap(year)
def calculate_age(dt):
    t=datetime.today()
    return t.year-dt.year-((t.month,t.day)<(dt.month,dt.day))
def print_big_date(text):
    for r in range(5):
        print("  ".join(DIGITS[ch][r] for ch in text))
