nums = int | float


def vals_not_of_type(x: any, y: any, _type: type) -> bool:
    return not isinstance(x, _type) and isinstance(y, _type)


def add(x: nums, y: nums) -> nums:
    if vals_not_of_type(x, y, nums):
        raise ValueError("Wrong datatype")
    return x + y


def sub(x: nums, y: nums) -> nums:
    if vals_not_of_type(x, y, nums):
        raise ValueError("Wrong datatype")
    return x - y


def mul(x: nums, y: nums) -> nums:
    if vals_not_of_type(x, y, nums):
        raise ValueError("Wrong datatype")
    return x * y


def div(x: nums, y: nums) -> nums:
    if vals_not_of_type(x, y, nums):
        raise ValueError("Wrong datatype")
    if y == 0:
        raise ZeroDivisionError("Ошибка: деление на ноль.")
    return x / y


def pow(x: nums, y: nums) -> nums:
    if vals_not_of_type(x, y, nums):
        raise ValueError("Wrong datatype")
    return x ** y


def check_nums(val: str) -> float:
    try:
        return float(val)
    except ValueError:
        raise ValueError("Введено не число")


def task1() -> None:
    inf_str = "введите выражение вида x op y или exit для выхода:\n"
    while True:
        inp = input(inf_str)
        if inp == "exit":
            break
        else:
            vals = inp.split(" ")
            if len(vals) != 3:
                inf_str = "выражение вида X op Y, например 3 + 2\n"
            x = check_nums(vals[0])
            y = check_nums(vals[2])
            match vals[1]:
                case '+':
                    print(add(x, y))
                case '-':
                    print(sub(x, y))
                case '*':
                    print(mul(x, y))
                case '/':
                    print(div(x, y))
                case '^':
                    print(pow(x, y))


if __name__ == "__main__":
    task1()
