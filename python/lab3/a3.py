prev = int(input("Предылущий: "))
purr = int(input("Текущий: "))

if purr == prev:
    op = "091284509128"
    while op not in "yn":
        op = input("Пользовались газом?(y/n)")
    if op == "y":

        result = 0

        if purr > prev:
            isp2 = abs(purr - prev)
        else:
            isp2 = abs(10000 - prev) + purr

        isp = isp2

        if isp <= 300:
            result = 21
        else:
            result += 21
            if isp > 800:
                result += (isp - 800) * 0.025
                isp = 800
            if isp > 600 and isp <= 800:
                result += (isp - 600) * 0.04
                isp = 600
            if isp > 300 and isp <= 600:
                result += (isp - 300) * 0.06
                isp -= 300

        print("Использовано: ", isp2)
        print("К оплате: ", round(result, 2))
        print("Ср цена за m^3: ", round(result / isp2, 2))
    else:
        print("Использовано: ", 0)
        print("К оплате: ", 0)
        print("Ср цена за m^3: ", 0)

else:
    result = 0

    if purr > prev:
        isp2 = abs(purr - prev)
    else:
        isp2 = abs(10000 - prev) + purr

    isp = isp2

    if isp <= 300:
        result = 21
    else:
        result += 21
        if isp > 800:
            result += (isp - 800) * 0.025
            isp = 800
        if isp > 600 and isp <= 800:
            result += (isp - 600) * 0.04
            isp = 600
        if isp > 300 and isp <= 600:
            result += (isp - 300) * 0.06
            isp -= 300

    print("Использовано: ", isp2)
    print("К оплате: ", round(result, 2))
    print("Ср цена за m^3: ", round(result / isp2, 2))
