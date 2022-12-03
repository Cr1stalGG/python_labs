import random

password = random.randrange(1, 100, 1)
count = random.randrange(1, 10, 1)

while count > 0:
    print("Количество попыток: ", count)
    userPassword = int(input("Введите пароль: "))

    if userPassword != password:
        print("Неверный пароль")
        print("Абсолютное значение: ", abs(password - userPassword))
    else:
        print("Пароль верный")
        break
    count -= 1

if count <= 0:
    print("Вы заблокированы!")



