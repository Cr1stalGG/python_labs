def checkQuater(x, y):
    if x > 0:
        if y > 0:
            return "I"
        else:
            return "IV"
    else:
        if y > 0:
            return "II"
        else:
            return "III"


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if checkQuater(x1, y1) == checkQuater(x2, y2):
    print("Yes")
    print(checkQuater(x1, y1))
else:
    print("No")

