n = int(input("$Введите к-во элементов: "))

if n <= 0:
    print("$Данные не корректны")
else:
    ev = []
    od = []
    res = []

    for i in range(0, n*2):
        if i % 2 == 0:
            ev.append(i)
        else:
            od.append(i)

    print("$Чётные: ", *ev)
    print("$Нечетные: ", *od)

    for i in range(n):
        res.append(ev[i] * od[i])
    print("$После перемножения: ", *res)
