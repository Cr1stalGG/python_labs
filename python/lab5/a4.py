def comparator(username, log = (), reg = ()):
    if username in log:
        num = input("Введите ваш номер: ")
        if num in reg:
            return True
        else:
            return False
    else:
        return False


log1 = input("Введите первый логин: ")
reg1 = input("Введите первый номер: ")

log2 = input("Введите второй логин: ")
reg2 = input("Введите второй номер: ")

log = (log1, log2)
reg = (reg1, reg2)
name = ''
while(not (comparator(name, log1, reg1) or comparator(name, log2, reg2))):
    name = input("Введите ваше имя: ")

    if comparator(name, log1, reg1) or comparator(name, log2, reg2):
        print("Здравствуйте,", name)
    else:
        print("Такого пользователя нет")
