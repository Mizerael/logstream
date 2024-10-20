set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}


def get_miss(s: set, u: set) -> list:
    """
    Получение списка всех отсутствующих в множестве
    """
    tmp = []
    for val in s:
        if val in u:
            pass
        else:
            tmp.append(val)
    return tmp


def task5() -> None:
    union = set1 | set2 | set3
    miss = get_miss(union, set1) + get_miss(union, set2)
    miss += get_miss(union, set3)
    diff = set(miss) - union
    print(union)
    print(miss)
    print(diff)


if __name__ == "__main__":
    task5()
