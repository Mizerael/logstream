def function_name(search: str, status: bool,
                  *args: list | tuple | set, **kwargs: dict) -> list | str:
    result = []
    result_2 = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f" {i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += (" Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")


def task3() -> None:
    print(function_name("args", True, *[1, "sst", 2]))
    print(function_name("args", True, *(1, "sst", 2)))
    print(function_name("args", True, *{1, "sst", 2}))
    print(function_name("args", True, *{'a': 1, 'b': "sst", 'c': 2}))
    print(function_name("args", False, *{'a': 1, 'b': "sst", 'c': 2}))
    print(function_name("kwargs", False, **{'a': 1, 'b': "sst", 'c': 2}))


if __name__ == "__main__":
    task3()
