first, second = map(int, input("Input first and last value of loop(in 1 line): ").split())
first_arr = []
res = []
for i in range(min(first, second), max(first, second)+1):
    first_arr.append(i)
    if i % 2 != 0:
        res.append(i)
    else:
        res.append(i-1)
print("First array:", *first_arr)
print("Result is:", *res)
