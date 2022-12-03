s1 = input()
s2 = input()
try:
    p1 = s1.index('.')
    p2 = s2.index('.')
    print(min(p1+1, p2+1))
except:
    print("error")