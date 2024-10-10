import sys


def task1():
    while True:
        inp = input()
        match inp.lower():
            case "exit":
                print("Конец...")
                sys.exit(0)
            case _:
                val = inp.lstrip('-')
                sign = len(val) < len(inp)
                if val.isdigit():
                    print(f"Длина :{len(val) + sign}")
                else:
                    print(f"Введено {type(inp)}")
