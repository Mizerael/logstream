import os
import pytest

sep: str = "\\" if os.name == "nt" else "/"
directory = os.path.dirname(__file__) + f"{sep}test_files"

if not os.path.exists(directory):
    os.makedirs(directory)


@pytest.fixture(autouse=True)
def open_files() -> None:
    with open(f"{directory}{sep}file1.txt", "w"):
        pass
    with open(f"{directory}{sep}file2.txt", "w"):
        pass
    with open(f"{directory}{sep}output.txt", "w"):
        pass
