from typing import Generator


def fibb_sequence(n: int) -> Generator[int, None, None]:
    a: int = 1
    b: int = 1
    while n > 0:
        yield a
        n -= 1
        a, b = b, a + b


def task2() -> None:
    fib_seq = fibb_sequence(5)
    print(type(fib_seq))
    for val in fib_seq:
        print(val)


if __name__ == "__main__":
    task2()
