code = []

while True:
    line = input()
    if '#' in line:
        break
    if line:
        code.append(line)

x = 0
y = 0
for lin in code:
    if lin[0:3] == 'for':
        print('цикл')

    elif lin[0:4] != '    ' and lin[lin.index('(') + 1] == ')':
        if 'right' in lin:
            x += 1
            print(x, y)
        elif 'left' in lin:
            x -= 1
            print(x, y)
        elif 'down' in lin:
            y += 1
            print(x, y)
        elif 'up' in lin:
            y -= 1
            print(x, y)

    elif lin[0:4] != '    ' and lin[lin.index('(') + 1] != ')':
        print('нцса')

    elif lin[0:4] == '    ' and lin[lin.index('(') + 1] == ')':
        print('вцба')

    elif lin[0:4] == '    ' and lin[lin.index('(') + 1] != ')':
        print('вцса')