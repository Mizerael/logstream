def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except ValueError:
                return "Bad request"
    try:
        result = round(sum(list_num) / len(list_num), 2)
    except Exception as e:
        return e
    return result


def test_average_sum() -> None:
    assert isinstance(average_num([]), ZeroDivisionError)
    assert average_num([1, 3, 5, 7, 9]) == 5
    assert average_num([1.1, 2.2, 3.3, 4.4, 5.5]) == 3.3
    assert average_num(["1", "2", "3"]) == 2
    assert average_num(["-1", "-2", "-3"]) == -2
    assert average_num(["1.1", "2.2", "3.3"]) == "Bad request"
    assert average_num([0b11, 0o7, 0xFF, 0b101]) == 67.5
    assert average_num(["0b11", "0o7", "0xff", "0b101"]) == "Bad request"
    assert average_num(["a", 2, 4]) == "Bad request"
    assert average_num([True, False, True, True]) == 0.75


if __name__ == "__main__":
    test_average_sum()
