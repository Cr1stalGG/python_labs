x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 <= 0 or x1 > 8 or x2 <= 0 or x2 > 8 or y1 <= 0 or y1 > 8 or y2 <= 0 or y2 > 8:
    print("Incorrect input data")
else:
    if (x1 + y1 + x2 + y2) % 2 == 0:
        print("YES")
        if x1 % 2 == 0:
            print("Black")
        else:
            print("White")
    else:
        print("NO")
