def task2():
    inp = int(input())
    negative = positive = 0
    start = min(inp, -inp)
    end = max(inp, -inp) + 2  # в задаче указан [-v, v} , возможно это опечатка
    for num in range(start, end):
        if num < 0:
            negative += num
        else:
            positive += num
        print(num)
    print(f"Сумма отрицательных: {negative}\n Сумма положительных: {positive}")
