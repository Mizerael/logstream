from src.block6.average_sum import average_num


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
