import time
sec = -999
while sec <= 0:
    sec = int(input("Введите корректное время"))
for i in range(sec, 0, -1):
    print(i)
    time.sleep(1)
print("С новым годом!!!")
