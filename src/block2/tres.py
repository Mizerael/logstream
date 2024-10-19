dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}


def task3() -> None:
    keys = set()
    items = set()
    for key, val in dct.items():
        keys.add(key)
        items.add(val)
    union = keys | items
    print(keys)
    print(items)
    print(union)


if __name__ == "__main__":
    task3()
