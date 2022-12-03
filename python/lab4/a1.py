currentLogin = input("Завайте логин: ")
currentPassword = input("Задайте пароль: ")

login = ""
password = ""

while login != currentLogin or password != currentPassword:
    login = input("Введите логин: ")
    if login == currentLogin:
        password = input("Введите пароль: ")
        if password != currentPassword:
            print("Пароль не верный")
    else:
        print("Логин не верный")

print("Пользователь авторизован")
