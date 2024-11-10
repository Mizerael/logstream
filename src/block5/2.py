import os
from datetime import datetime


def task2() -> None:
    sep: str = "\\" if os.name == "nt" else "/"
    cur_date: str = str(datetime.now())
    print(cur_date)
    try:
        os.makedirs(cur_date)
    except OSError:
        print("Директория в этот момент уже создана")
    file_name: str = "aboba.txt"
    file_path: str = cur_date + f"{sep}{file_name}"
    open(file_path, "a").close()
    try:
        sub_path: str = cur_date + f"{sep}sub"
        os.makedirs(sub_path)
        os.rename(file_path, sub_path + sep + file_name)
    except OSError:
        print("Директория уже создана")


if __name__ == "__main__":
    task2()
