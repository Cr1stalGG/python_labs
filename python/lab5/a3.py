import turtle
import turtle as t


def c(color):
    colors = {
        "b": "black",
        "w": "white",
        "g": "green"
    }
    if color not in colors and '#' not in color:
        return "Error color"
    if color in colors:
        color = colors[color]
    return str(color)


allowedCmds = ['f', 'b', 'r', 'l', 'c']
turtle.getscreen()
turtle.shape('turtle')

while True:
    cmd = list(input().split())

    if cmd[0] not in allowedCmds or len(cmd) > 2:
        print("Error")
        continue

    if cmd[0] == "quit()":
        break

    intCmds = ['f', 'b', 'r', 'l']
    if cmd[0] in intCmds:
        try:
            cmd[1] = int(cmd[1])
        except BaseException:
            print("TypeError")
            continue
    if cmd[0] == 'f':
        t.forward(cmd[1])
    if cmd[0] == 'b':
        t.backward(cmd[1])
    if cmd[0] == 'r':
        t.right(cmd[1])
    if cmd[0] == 'l':
        t.left(cmd[1])
    if cmd[0] == 'c':
        try:
            t.color(c(cmd[1]))
        except:
            print('error')
            continue

print("End")
