from typing import Callable


def get_num(inf: str, check: Callable[[str], bool]) -> int:
    """
    получение числа с консоли
    args:
        inf: информационная строка input()
        check: функция условия принятия вводимого объекта
    """
    inp = input(inf)
    inf_cp = "Попробуйте снова: "
    while True:
        if check(inp):
            break
        inp = input(inf_cp)
    return int(inp)


def task1() -> None:
    cnt = get_num("Введите количество элементов: ", lambda x: x.isdigit())
    res = []
    deg = []

    for i in range(cnt):
        i_res = input(f"{i+1}-ый элемент: ")
        try:
            i_res = float(i_res)
            res.append(i_res)
        except ValueError:
            res.append(i_res)

        i_deg = get_num(
            f"степень {i+1}-го элемента: ",
            lambda x: x.startswith("-") and x[1:].isdigit() or x.isdigit(),
        )
        deg.append(i_deg)

    for i in range(cnt):
        if isinstance(res[i], float):
            print(f"{i}: {res[i] ** deg[i]}")
        else:
            print(f"{i}: {res[i] * deg[i]}")


if __name__ == "__main__":
    task1()
