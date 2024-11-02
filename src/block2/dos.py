def task2() -> None:
    inp = input().lower().replace(" ", "")
    chars = {}

    for val in set(inp):
        chars[val] = inp.count(val)
    print(chars)


if __name__ == "__main__":
    task2()
