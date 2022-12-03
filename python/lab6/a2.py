import random
while 1:
    try:
        count = int(input("Input len of list: "))
        min, max = map(int, input("Input range(min max): ").split())
        l = list()
        for i in range(count):
            l.append(random.randrange(min, max+1))
        print(*l)
        print(sum(l))
    except:
        print("Error")
