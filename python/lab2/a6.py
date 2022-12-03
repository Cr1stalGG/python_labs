sec = int(input())
if sec < 0:
    print("Incorrect input data")
else:
    if sec > 86400:
        sec -= 86400
    mins = (sec - sec % 60) // 60
    sec -= mins * 60

    h = (mins - mins % 60) // 60
    mins -= h * 60

    print('{}:{:02}:{:02}'.format(h, mins, sec))
