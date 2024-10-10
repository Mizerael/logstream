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
