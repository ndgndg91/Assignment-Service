import random


def draw(drawn=None):
    if drawn is None:
        heart = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'XH', 'JH', 'QH', 'KH', 'AH']
        diamond = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'XD', 'JD', 'QD', 'KD', 'AD']
        clover = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'XC', 'JC', 'QC', 'KC', 'AC']
        spade = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'XS', 'JS', 'QS', 'KS', 'AS']
        dec = []
        dec.append(heart)
        dec.append(diamond)
        dec.append(clover)
        dec.append(spade)
        return random.choice(random.choice(dec))
    else:
        dec = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'XH', 'JH', 'QH', 'KH', 'AH','2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'XD', 'JD', 'QD', 'KD', 'AD',
               '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'XC', 'JC', 'QC', 'KC', 'AC','2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'XS', 'JS', 'QS', 'KS', 'AS']
        for i in drawn:
            if i in dec:
                dec.remove(i)
        return random.choice(dec)

print(draw())
print(draw(['6H', '3C', '3D', '8C', 'AD', '9D', '7D', 'QC']))
print(draw(drawn=('3S', '8H', '8C', '2H', 'AC')))
print(draw({'4C', 'AH', 'JS', '7S', '9H', '2H', 'QC', '2S', '3H', '7C'}))


def arrange(rows=None, cols=None):
    heart = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'XH', 'JH', 'QH', 'KH', 'AH']
    diamond = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'XD', 'JD', 'QD', 'KD', 'AD']
    clover = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'XC', 'JC', 'QC', 'KC', 'AC']
    spade = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'XS', 'JS', 'QS', 'KS', 'AS']
    length = len(heart) + len(diamond) + len(clover) + len(spade)
    if rows * cols > length:
        assert rows * cols < length, 'invalid grid'
    else:
        dec = []
        dec.append(heart)
        dec.append(diamond)
        dec.append(clover)
        dec.append(spade)
        r = []
        for i in range(rows):
            row = []
            r.append(row)
        for i in r:
            for j in range(cols):
                i.append(random.choice(random.choice(dec)))

        return r


print(arrange(rows=3, cols=4))
# print(arrange(rows=7, cols=8))

print('=====================================')


def extend(grid):
    heart = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'XH', 'JH', 'QH', 'KH', 'AH']
    diamond = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'XD', 'JD', 'QD', 'KD', 'AD']
    clover = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'XC', 'JC', 'QC', 'KC', 'AC']
    spade = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'XS', 'JS', 'QS', 'KS', 'AS']
    dec = []
    dec.append(heart)
    dec.append(diamond)
    dec.append(clover)
    dec.append(spade)
    rows = len(grid)
    cols = len(grid[0])
    addlist = []
    for i in range(cols):
        addlist.append(random.choice(random.choice(dec)))
    grid.append(addlist)
    # return grid


grid = [['QH', '9S', '3C'], ['5D', '8C', '2H']]
extend(grid)
print(grid)

print('=======================================')


def select(grid):
    # rows = len(grid)
    # cols = len(grid[0])
    choice_row = grid.index(random.choice(grid))
    choice_col = grid[choice_row].index(random.choice(grid[choice_row]))
    return (choice_row, choice_col)


print(select(grid))
