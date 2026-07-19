from functions import get_birth_date,get_weekday,is_leap,calculate_age,print_big_date

def main():
    print("="*50)
    print("ПРОГРАММА АНАЛИЗА ДАТЫ РОЖДЕНИЯ")
    print("="*50)
    birth_date=get_birth_date()
    print("\nРезультаты:")
    print("-"*50)
    print("Дата рождения:",birth_date.strftime("%d.%m.%Y"))
    print("День недели:",get_weekday(birth_date))
    print("Високосный год:","Да" if is_leap(birth_date.year) else "Нет")
    print("Возраст:",calculate_age(birth_date),"лет")
    print("\nДата рождения звёздочками:\n")
    print_big_date(birth_date.strftime("%d %m %Y"))
if __name__=="__main__":
    main()
