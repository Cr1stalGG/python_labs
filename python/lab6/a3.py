notes = list()

while True:
    str = '''
    1) добавить в список какое-либо дело
    2) вывести список дел с их индексами
    3) удалить дело по индексу
    '''
    op = input(str)
    if op not in ['1', '2', '3']:
        print('Error')
        continue
    else:
        if op == '1':
            notes.append(input('Введите дело: '))
        if op == '2':
            for i in range(len(notes)):
                print(notes[i], ":", i)
        if op == '3':
            try:
                notes.pop(int(input("Введите индекс: "))-1)
            except:
                print("Error")