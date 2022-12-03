A = int(input())
B = int(input())

if A <= 1 or A >= 1000 or B <= 1 or B >= 1000:
    print("Incorrect input data")
else:
    if A == B:
        print("Равны")
    else:
        print("Не равны")
        print(max(A, B))
