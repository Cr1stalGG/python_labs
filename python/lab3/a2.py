import string

allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits + "#-*"

def isCorrectPassword(password):
    specSymbols = "#-*"
    if len(password) == 8 and any(i in allowed for i in password) and any(symbol.isdigit() for symbol in password) and password.lower() != password and password.upper() != password and any(i in specSymbols for i in password):
        return "Надёжный пароль"
    else:
        return False

password = input()

if isCorrectPassword(password) == False:
    if len(password) != 8:
        print("Длина пароля не равна 8")
    if not any(symbol.isdigit() for symbol in password):
        print("В пароле отсутствуют цифры")
    if password.lower() == password:
        print("В пароле отсутствуют заглавные буквы")
    if password.upper() == password:
        print("В пароле отсутствуют строчные буквы")
    if not any(i in "#-*" for i in password):
        print("В пароле отсутствуют специальные символы")
    if any(i not in allowed for i in password):
        print("В пароле используются непредусмотренные символы")
else:
    print(isCorrectPassword(password))
