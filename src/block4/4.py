from typing import Generator, Callable


def decor(func: Callable[[int], Generator[int, None, None]]):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@decor
def fibb_sequence(n: int) -> Generator[int, None, None]:
    a: int = 1
    b: int = 1
    while n > 0:
        yield a
        n -= 1
        a, b = b, a + b


def task4() -> None:
    fib_seq = fibb_sequence(5)
    for val in fib_seq:
        print(val)


if __name__ == "__main__":
    task4()
