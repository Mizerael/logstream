import sys

ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2 К2"
field = ship.lower().split()


def task4():
    inp = input().lower()
    for ship in field:
        if inp in ship:
            print("Попадание")
            sys.exit(0)

    print("Мимо")


def task4_1():
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    age = input("Возраст: ")
    print("<<Ваше имя: <<{}>>, Фамилия: <<{}>>, Возраст: <<{}>> лет.>>\n"
          .format(first_name, last_name, age))

    print(
        f"<<Ваше имя: <<{first_name}>>, "
        f"Фамилия: <<{last_name}>>, Возраст: <<{age}>> лет.>>")
