op = list()
s = input()

try:
    print(eval(compile(s, "string", "eval")))
    op.append(s + "=" + str(eval(compile(s, "string", "eval"))))
except:
    print("Error")

print(*op)