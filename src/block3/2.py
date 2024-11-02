from typing import Callable

mulable = int | float | str | list | tuple


def mul_list(lst: list[mulable], num: int = 2) -> list[mulable]:
    return [x * num for x in lst]


def pep8_heh(
    lst: list[mulable],
    f: Callable[[list[mulable], int], list[mulable]],
    num: int = 2,
) -> None:
    print(f(lst, num))


def task2() -> None:
    some_list = [1, 2, 4.3, "str", (1, 2.2, "a"), [1, 2.2, "str", (1.5, "a")]]

    print(some_list)

    print(mul_list(some_list))
    print(mul_list(some_list, 3))

    pep8_heh(some_list, lambda lst, num: [x * num for x in lst])
    pep8_heh(some_list, lambda lst, num: [x * num for x in lst], num=3)


if __name__ == "__main__":
    task2()
