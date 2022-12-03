q = input()
cmd = list()

while q != 'q':
    cmd.append(list(q.split()))
    q = input()

for i in range(len(cmd)):
    print("{} : {}".format(cmd[i][0], cmd[i][1]))
    