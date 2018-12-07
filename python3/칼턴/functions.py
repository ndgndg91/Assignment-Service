###########################################################################################################
#                   문제 1번
def ceiling(number):
    if 0 < number < 1:
        return 1
    if -1 < number < 0:
        return 0
    if number > 1:
        plus = float(number) // int(number)
        number = number + plus
        return int(number)
    if number < -1:
        return int(number)


print(ceiling(0.9))
print(ceiling(2.1))
print(ceiling(-2.1))
print(ceiling(-0.9))


##########################################################################################################
#                   문제 2번
def asc_codes(some_list):
    r = list(reversed([ord(x) for x in some_list if x.isupper()]))
    return r


print(asc_codes(['H', 'e', 'l', 'L', 'o', 'W', 'o', 'r', 'l', 'D']))
###########################################################################################################
#                   문제 3번
x = 3


def foo():
    x = 7
    print(x)
    return x


def bar():
    x = 5
    print(x)


def qux():
    global x
    x = 3
    print(x)


x = 9
print(x)  # 9  출력
qux()  # 3    출력
print(x)  # 3  출력
x = foo()  # 7   출력
print(x)  # 7    출력
bar()  # 5      출력
print(x)  # 7   출력


###########################################################################################################
#                       문제 4번
def capital_list(string):
    string = string.split()
    r = []
    for i in string:
        for j in i:
            if j.isupper():
                r.append(i)
                break
    return r


print(capital_list("This is the First question on your Second quiz."))
###########################################################################################################
#                       문제 5번
import random


def make_dimension(string, y, z):
    r = []
    string = string.split(',')
    for a in range(len(string)):
        string[a] = int(string[a])
    max_val = max(string)
    min_val = min(string)
    for i in range(y):
        row = []
        r.append(row)
    for j in range(len(r)):
        for k in range(z):
            while True:
                random_no = random.randint(min_val, max_val)
                if random_no % 2 == 0:
                    r[j].append(random_no)
                    break
    return r


print(make_dimension("1,2,3,4,5 ", 2, 2))
###########################################################################################################
