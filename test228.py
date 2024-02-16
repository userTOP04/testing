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
        cycle = int(lin[lin.index('(') + 1:lin.index(')')])

    elif lin[0:4] != '    ' and lin[lin.index('(') + 1] == ')':
        if 'right' in lin:
            x += 1
        elif 'left' in lin:
            x -= 1
        elif 'down' in lin:
            y += 1
        elif 'up' in lin:
            y -= 1

    elif lin[0:4] != '    ' and lin[lin.index('(') + 1] != ')':
        if 'right' in lin:
            x += int(lin[lin.index('(') + 1:lin.index(')')])
        elif 'left' in lin:
            x -= int(lin[lin.index('(') + 1:lin.index(')')])
        elif 'down' in lin:
            y -= int(lin[lin.index('(') + 1:lin.index(')')])
        elif 'up' in lin:
            y += int(lin[lin.index('(') + 1:lin.index(')')])

    elif lin[0:4] == '    ' and lin[lin.index('(') + 1] == ')':
        if 'right' in lin:
            right = 1
            right *= cycle
            x += right
        elif 'left' in lin:
            left = 1
            left *= cycle
            x -= left
        elif 'down' in lin:
            down = 1
            down *= cycle
            y -= down
        elif 'up' in lin:
            up = 1
            up *= cycle
            y += up

    elif lin[0:4] == '    ' and lin[lin.index('(') + 1] != ')':
        if 'right' in lin:
            right = int(lin[lin.index('(') + 1:lin.index(')')])
            right *= cycle
            x += right
        elif 'left' in lin:
            left = int(lin[lin.index('(') + 1:lin.index(')')])
            left *= cycle
            x -= left
        elif 'down' in lin:
            down = int(lin[lin.index('(') + 1:lin.index(')')])
            down *= cycle
            y -= down
        elif 'up' in lin:
            up = int(lin[lin.index('(') + 1:lin.index(')')])
            up *= cycle
            y += up
