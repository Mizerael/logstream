
def check_unique(val: int) -> bool:
    """
    Функция проверяет уникальность чисел трехзначного числа
    args:
        val: трехзначное целочисленное число типа
    """
    return val[0] == val[1] or val[0] == val[2] or val[1] == val[2]


def task3():
    while True:
        inp = input().lstrip('-')
        if not inp.isdigit():
            print("Не число, попробуйте снова\n")
        elif len(inp) != 3:
            print("Число не трехзначное, попробуйте снова\n")
        elif check_unique(inp):
            print("Есть повторяющиеся цифры, попробуйте снова\n")
        else:
            print("Перестановки:")
            for i in range(len(inp)):
                rem = inp[:i] + inp[i+1:]
                for j in range(len(rem)):
                    print(f"{inp[i] + rem[j] + rem[:j] + rem[j+1:]}")
            break
