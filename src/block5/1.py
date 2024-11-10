import random


def task1() -> None:
    num = random.randint(1, 100)
    print(f"Четное число {num}" if num % 2 == 0 else f"Нечетное число {num}")


if __name__ == "__main__":
    task1()
