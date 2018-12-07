# 2.3
def function_name(somelist):
    result = 0
    for i in somelist:
        result += i
    return result


a = [1, 2, 3, 4, 5]
print(function_name(a))


def recursive_func(somelist):
    if somelist == []:
        return 0
    else:
        return recursive_func(somelist[1:]) + somelist[0]


a = [1, 2, 3, 4, 5]
print(recursive_func(a))


# 2.4
def foobar(arg):
    if arg == []:
        return arg
    else:
        return foobar(arg[1:]) + [arg[0]]


print(foobar([1, 2, 3, 4, 5]))


# 4.1
def h(x):
    return f(x) + x


def f(x):
    x = x - 1
    return g(x) + 1


def g(x):
    return x * 2


print(h(4))
# f(4) +4  = 6 + 1 + 4 = 11
# g(3) +1 = 6 + 1
# g(3) = 6

# 4.3
squares = [x ** 2 for x in range(1, 11)]
print(list(filter(lambda x: x > 30 and x < 70, squares)))


def long_hand():
    squares = range(1, 11)
    result = []
    for i in squares:
        if i ** 2 > 30 and i ** 2 < 70:
            result.append(i ** 2)

    return result


print(long_hand())

# 4.4
dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']
print(list(map(lambda x: len(x), dna_list)))

# 5.1
records = [{"name": "actgctagt", "accession": "ABC123", "code": 1},
           {"name": "ttaggatc", "accession": "DEF456", "code": 2}]
one_record = records[1]
print(one_record)

aln = [["A", "T", "-", "T", "G"], ["A", "A", "T", "A", "G"], ["T", "-", "T", "T", "G"], ["A", "A", "-", "T", "A"]]
seq = aln[2]
print(seq)
char = aln[2][3]
print(char)

# 3.4 , 5.3
