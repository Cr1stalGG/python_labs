cur = 0
notes = list()

av_cur = 0

menu = '''
    a)Внести трату (число должно вноситься в список отрицательным!):
    b)Внести доход (число должно вноситься в список положительным!):
    c)Посмотреть список трат и доходов с выводом в виде:
    d)Рассчитать текущий баланс
    e)Рассчитать, сколько текущей суммы на балансе хватит на заданное с
клавиатуры количество суток
'''
while True:
    cmd = input(menu)
    if cmd not in ['a', 'b', 'c', 'd', 'e']:
        print("Error")
        continue
    try:
        if cmd == 'a':
            val, com = input("Введите трату: ").split()
            val = int(val)
            if val > 0:
                print('error')
                continue
            else:
                cur += val
                notes.append([val, com])
        if cmd == 'b':
            val, com = input("Введите доход: ").split()
            val = int(val)
            if val < 0:
                print('error')
                continue
            else:
                cur += val
                notes.append([val, com])

        if cmd == 'c':
            for note in notes:
                print("{} - \"{}\"".format(note[0], note[1]))
        if cmd == 'd':
            print(cur)
        if cmd == 'e':
            if len(notes) == 0:
                print('error')
                continue
            av_cur = cur/len(notes)
            if av_cur >= 0 :
                print('inf')
            elif cur <= 0 and av_cur <= 0:
                print('died')
            else:
                print(cur // av_cur)
    except:
        print("error")