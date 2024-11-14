def merge_and_write(
    file1_path: str, file2_path: str, output_file_path: str
) -> str:
    try:
        with open(file1_path, "r") as file1:
            data1 = file1.read().strip()

        with open(file2_path, "r") as file2:
            data2 = file2.read().strip()

        merged_data = data1 + " " + data2

        with open(output_file_path, "w") as output_file:
            output_file.write(merged_data)

        with open(output_file_path, "r") as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"
