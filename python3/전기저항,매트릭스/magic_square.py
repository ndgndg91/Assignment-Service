import graphics


def make_matrix(n):
    result = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        result.append(r)
    row = n - 1  # n = 5 row = 4
    col = int(n / 2)  # n = 5 col = 2
    for k in range(1, (n * n) + 1):
        if row == n:
            row = 0
        if col == n:
            col = 0
        if result[row][col] == 0:
            result[row][col] = k
        else:
            row -= 2
            col -= 1
            result[row][col] = k
        row += 1
        col += 1
    return result


number = int(input("Enter n : "))
return_val = make_matrix(number)
for i in return_val:
    print('-----'*number)
    for j in i:
        print('|', end=' ')
        if len(str(j)) == 1:
            j = str(j)
            j = ' ' + j
        print(j, end=' ')
    print('|')
print('-----'*number)

win = graphics.GraphicsWindow()
win.setTitle('magic_square')
line = number * 50
win.canvas.setHeight(line)
win.canvas.setWidth(line)
x = line / number
y = 0
z = 0
xyz = 0
for j in range(number):
    y = 0
    for i in range(number):
        win.canvas.drawRect(y, z, x, x)
        win.canvas.drawText(y+(x/2.5), z+(x/2.5), return_val[j][i])
        y += x
    z += x

win.wait()
