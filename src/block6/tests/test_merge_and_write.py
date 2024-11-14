import pytest
from typing import List
from src.block6.tests.conftest import sep, directory
from src.block6.merge_and_write import merge_and_write

dir_path = f"{directory}{sep}"


def create_data(filename: str, test_data: str) -> None:
    path = dir_path + filename
    with open(path, "a") as f:
        f.writelines(test_data)


@pytest.mark.parametrize(
    "texts_data, result",
    [
        (["file1", "file2"], "file1 file2"),
        (["   a vee     ", "akwddwad"], "a vee akwddwad"),
    ],
)
def test_merge_and_write(texts_data: List[str], result: str):
    files_names: List[str] = [
        "file1.txt",
        "file2.txt",
    ]
    output_file_path = f"{directory}{sep}output.txt"
    for i in range(len(files_names)):
        create_data(files_names[i], texts_data[i])
    assert (
        merge_and_write(
            f"{dir_path}{files_names[0]}",
            f"{dir_path}{files_names[1]}",
            output_file_path,
        )
        == result
    )


@pytest.mark.parametrize(
    "files_paths, texts_data, result",
    [
        (
            ["file3", "file2"],
            ["aboba", "aboba"],
            "Один из файлов не найден",
        ),
    ],
)
def test_merge_and_write_exceptions(
    files_paths: str,
    texts_data: str,
    result: str,
):
    files_names: List[str] = [
        "file1.txt",
        "file2.txt",
    ]
    output_file_path = f"{directory}{sep}output.txt"
    for i in range(len(files_names)):
        create_data(files_names[i], texts_data[i])
    assert (
        merge_and_write(
            f"{dir_path}{files_paths[0]}",
            f"{dir_path}{files_paths[1]}",
            output_file_path,
        )
        == result
    )
