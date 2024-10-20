dictionary = {
    "Имя": ["Андрей", "Кирилл", "Анна", "Евгений", "Евгений", "Александр", "Татьяна", "Аркадий", "Игорь", "Кирилл"],
    "Фамилия": ["Иванов", "Лазарев", "Петрова", "Надобников", "Никитин", "Иванов", "Никитина", "Лихачев", "Никитин", "Левашев"],
    "Город проживания": ["Москва", "Омск", "Псков", "Псков", "Москва", "Псков", "Москва", "Омск", "Псков", "Москва"],
    "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
    "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
    "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
    "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия", "Работает", "Студент"]
}


def task4() -> None:
    updated_dict = {}
    for i in range(len(dictionary.get("Имя"))-1):
        name = dictionary.get("Имя")[i]
        if name == "Кирилл":
            dictionary.get("Имя")[i] += 'л'
        surname = dictionary.get("Фамилия")[i]
        if ((surname == "Никитин" or surname[:-1] == "Никитин" and
            surname.endswith('а')) and
                dictionary.get("Город проживания")[i] == "Москва"):
            dictionary.get("Город проживания")[i] = "Махачкала"
        if (name == "Александр" and surname == "Иванов" and
                dictionary.get("Статус")[i] == "Студент"):
            dictionary.get("Статус")[i] == "Работает"
        if name == "Аркадий" and surname == "Лихачев":
            for val in dictionary.values():
                val.pop(i)

    fullnames = list(zip(dictionary.get("Фамилия"), dictionary.get("Имя")))
    updated_dict["Фамилия Имя"] = ["--".join(tp) for tp in fullnames]

    birthdates = list(zip(dictionary.get("Год рождения"),
                          dictionary.get("Месяц рождения"),
                          dictionary.get("Число рождения")))
    pres = [4, 2, 2]
    updated_dict["Дата рождения"] = ["-".join(
        (f"{vl:0{pres[i]}d}" for i, vl in enumerate(tp))) for tp in birthdates]
    updated_dict["Город проживания"] = dictionary.get("Город проживания")
    updated_dict["Статус"] = dictionary.get("Статус")

    print(dictionary)
    print("-"*80)
    print(updated_dict)


if __name__ == "__main__":
    task4()
