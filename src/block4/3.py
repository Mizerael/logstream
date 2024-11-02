from typing import List


def writer_reader(
    name: str, text: str = "", ext: str = "txt", enc: str = "utf-8"
) -> None:
    file_name: str = f"{name}.{ext}"
    with open(file_name, mode="a+", encoding=enc) as file:
        if text != "":
            file.write(f"{text}\n")
        file.seek(0)
        lines: List[str] = file.read().splitlines()
        for i in range(0, len(lines), 2):
            print(lines[i])


def task3() -> None:
    writer_reader("aboba", "какой-то текст")


if __name__ == "__main__":
    task3()
