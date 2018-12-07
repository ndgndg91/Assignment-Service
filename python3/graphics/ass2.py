from graphics import *


def guide():
    print('''Select the type shape.
1. Circle
2. Triangle
3. Rectangle''')
    choice = int(input('>>'))
    if choice in [1, 2, 3]:
        return choice
    else:
        print('You must select among the 1, 2, 3')
        return guide()


def guide2():
    print('Input the number of depth.')
    try:
        return_val = int(input('>>'))
    except ValueError:
        print('You must input the Integer')
        return guide2()
    return return_val


def guide3():
    print('Input the the length of Unit.')
    try:
        return_val = int(input('>>'))
    except ValueError:
        print('You must input the Integer')
        return guide3()
    return return_val


def make_circle(depth, length):
    pass


def make_rectangle(depth, length):
    pass


def make_triangle(depth, length):
    pass


def main():
    choice = guide()
    if choice == 1:
        depth = guide2()
        length = guide3()
        make_circle(depth, length)
    elif choice == 2:
        depth = guide2()
        length = guide3()
        make_triangle(depth, length)
    elif choice == 3:
        depth = guide2()
        length = guide3()
        make_rectangle(depth, length)


if __name__ == '__main__':
    main()
