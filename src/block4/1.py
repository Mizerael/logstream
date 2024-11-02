import calendar
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")


def task1() -> None:
    print(f"1: {[x ** 2 for x in range(1, 11)]}")
    weekdays = [calendar.day_name[i] for i in range(7)]
    weekdays_dict = {i + 1: weekdays[i] for i in range(len(weekdays))}
    print(f"2: {weekdays_dict}")
    lib_lst = [
        "Django",
        "FastAPI",
        "Numpy",
        "PYTHON",
        "Pandas",
        "FASTAPI",
        "Python",
        "random",
    ]
    lib_set = {name.lower() for name in lib_lst}
    print(f"3: {lib_set}")


if __name__ == "__main__":
    task1()
