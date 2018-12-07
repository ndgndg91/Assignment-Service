import re


def old_location(some_list):  # 옮길 말을 입력받는 함수
    r = []
    row = re.compile(r'[a-h]')
    col = re.compile(r'[1-8]')
    show_requirement()
    while True:
        o_row = input('enter the row :')
        o_col = input('enter the column :')
        if row.match(o_row) and col.match(o_col):
            o_row = int(convert(o_row))
            o_col = int(o_col) - 1
            if some_list[o_row][o_col] != '-':
                r.append(o_row)
                r.append(o_col)
                return r
            else:
                print('해당 위치에 아무 말도 없습니다.')
                print_chess_board(some_list)
        else:
            print('형식에 맞게 입력해주세요')


def new_location():  # 옮길 위치를 입력받는 함수
    r = []
    row = re.compile(r'[a-h]')
    col = re.compile(r'[1-8]')
    show_requirement('of the piece')
    while True:
        n_row = input('enter the row :')
        n_col = input('enter the column :')
        if row.match(n_row) and col.match(n_col):
            n_row = int(convert(n_row))
            n_col = int(n_col) - 1
            r.append(n_row)
            r.append(n_col)
            return r
        else:
            print('형식에 맞게 입력해주세요')


def move(some_list):  # 입력받은 말을 입력받은 위치로 옮기는 함수
    old = old_location(some_list)
    new = new_location()
    o_row = int(old[0])
    o_col = int(old[1])
    n_row = int(new[0])
    n_col = int(new[1])
    some_list[n_row][n_col] = some_list[o_row][o_col]
    some_list[o_row][o_col] = '-'
    return some_list


def convert(string):  # 행의 인덱스를 코딩할 수 있도록 숫자로 바꿔주는 함수
    if string == 'a':
        return 0
    elif string == 'b':
        return 1
    elif string == 'c':
        return 2
    elif string == 'd':
        return 3
    elif string == 'e':
        return 4
    elif string == 'f':
        return 5
    elif string == 'g':
        return 6
    elif string == 'h':
        return 7


def show_requirement(string=None):  # 체스판에서 말을 움직이기 위해서 입력하는 형식을 알려주는 함수
    print()
    if string is None:
        print('Select the location you want to move.')
        print('row = a, b, c, d, e, f, g, h')
        print('column = 1, 2, 3, 4, 5, 6, 7, 8')
    else:
        print('Select the location' + string + ' you want to move.')
        print('row = a, b, c, d, e, f, g, h')
        print('column = 1, 2, 3, 4, 5, 6, 7, 8')


def ask_options():  # 사용자에게 다음 프로그램 진행 방향을 선택하게 하기 위한 함수 
    print('We can choose one of three options.')
    print('1. Enter another chessboard from scratch')  # 1번은 새로운 체스판을 입력받는 선택
    print('2. Simply move a piece')  # 2번은 입력받은 체스판에서 체스 말을 움직이게 하는 선택
    print('3. Quit')  # 3번은 어느팀이 이겼는지 알려주면서 프로그램을 종료하는 선택
    print('Enter a number between 1, 2, and 3')
    try:
        result = int(input('what is your choice? : '))
    except ValueError:
        print('You have entered incorrectly. Please retype to match the format.')
        return ask_options()
    else:
        if result not in [1, 2, 3]:
            print('You have entered incorrectly. Please retype to match the format.')
            return ask_options()
        else:
            return result


def which_win(white, black):  # 어느 팀이 이겼는지 점수를 가지고 결과를 말해주는 함수
    if white > black:
        print("The Winner is White")
        print("White %0.1f : %0.1f Black" % (white, black))
    elif white < black:
        print("The Winner is Black")
        print("White %0.1f : %0.1f Black" % (white, black))
    elif white == black:
        print("Draw")
        print("White %0.1f : %0.1f Black" % (white, black))


def sum_white(some_list):  # 흰색 팀의 점수를 구해주는 함수
    score = 0
    for i in range(len(some_list)):
        for j in some_list[i]:
            if j == 'q':
                score = score + 10
            elif j == 'r':
                score = score + 5
            elif j == 'n':
                score = score + 3.5
            elif j == 'b':
                score = score + 3
            elif j == 'p':
                score = score + 1
    return score


def sum_black(some_list):  # 검은색 팀의 점수를 구해주는 함수
    score = 0
    for i in range(len(some_list)):
        for j in some_list[i]:
            if j == 'Q':
                score = score + 10
            elif j == 'R':
                score = score + 5
            elif j == 'N':
                score = score + 3.5
            elif j == 'B':
                score = score + 3
            elif j == 'P':
                score = score + 1
    return score


def print_chess_board(some_list):  # 입력받은 체스판을 사용자에게 출력해주는 함수
    print('  12345678')
    rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(len(some_list)):
        print(rows[i], end=" ")
        for j in some_list[i]:
            print(j, end="")
        print()


def explicate_input():  # 사용자에게 대략적인 설명을 해주는 함수
    print('Enter the chessboard you want.')
    print("We'll tell you if Black will win or White will win")
    print('===================================================================')
    print('|   The white pieces is lowercase and black pieces is uppercase   |')
    print('|          The white King is "k" and black King is "K"            |')
    print('|          The white Queen is "q" and black Queen is "Q"          |')
    print('|          The white Rook is "r" and black King is "R"            |')
    print('|          The white Knight is "n" and black King is "N"          |')
    print('|          The white Bishop is "b" and black King is "B"          |')
    print('|          The white Pawn is "p" and black King is "P"            |')
    print('===================================================================')
    print('    We need 8 list inputs. like this                          ')
    print('    first input   : -----k--')
    print('    second input  : --------')
    print('    third input   : ---n----')
    print('    fourth input  : --------')
    print('    fifth input   : --------')
    print('    sixth input   : ----K---')
    print('    seventh input : --------')
    print('    eighth input  : ---Q----')


def input_test_len(string):  # 체스판이 8 x 8 의 형태이기 때문에 길이가 8만을 받기 위한 함수
    if len(string) != 8:
        print('You have entered incorrectly. Please retype to match the format.')
        return False
    else:
        return True


def input_test_format(string):  # 정해진 문자열만 받을 수 있도록 하기 위한 함수
    for i in string:
        if i not in ['-', 'k', 'q', 'r', 'n', 'b', 'p', 'K', 'Q', 'R', 'N', 'B', 'P']:
            print('You have entered incorrectly. Please retype to match the format.')
            return False
    return True


def input_test_one_piece(string):  # 한 행당 하나의 체스말만 받을 수 있게 하기 위한 함수
    cnt = 0
    for i in string:
        if i in ['k', 'q', 'r', 'n', 'b', 'p', 'K', 'Q', 'R', 'N', 'B', 'P']:
            cnt += 1
    if 0 <= cnt <= 1:
        return True
    else:
        print('This program can only place one chess piece per row.')
        return False


def get_input(string):  # 입력하는 체스판 정보가 주어진 규격에 맞는지 확인하는 함수
    row = input('Enter the ' + string + ' row :')
    rows = []
    if input_test_len(row):
        if input_test_format(row):
            if input_test_one_piece(row):
                for i in row:
                    rows.append(i)
                return rows
            else:
                return get_input(string)
        else:
            return get_input(string)
    else:
        return get_input(string)


def get_inputs():  # 체스판의 정보를 입력 받는 함수
    first_row = get_input('first')
    second_row = get_input('second')
    third_row = get_input('third')
    fourth_row = get_input('fourth')
    fifth_row = get_input('fifth')
    sixth_row = get_input('sixth')
    seventh_row = get_input('seventh')
    eighth_row = get_input('eighth')
    chess_board = [first_row, second_row, third_row, fourth_row, fifth_row, sixth_row, seventh_row, eighth_row]
    # print(chess_board)
    return chess_board


def convert_list(some_list):  # pygame으로 체스판을 그려줄 때 체스말을 어디 위치에 그릴 지 알기 위한 함수
    r = [8, 8, 8, 8, 8, 8, 8, 8]  # 몇행 몇열에 그릴지
    for i in range(len(some_list)):
        for j in range(len(some_list[i])):
            if some_list[i][j] != '-':
                r[i] = j
    return r


def piece_info(some_list):  # pygame으로 체스판을 그려줄 때 어떤 체스 말을 그릴 지 알기 위한 함수
    r = [8, 8, 8, 8, 8, 8, 8, 8]  # 킹, 퀸 ,룩 ,비숍, 포운 등등
    for i in range(len(some_list)):
        for j in range(len(some_list[i])):
            if some_list[i][j] != '-':
                r[i] = some_list[i][j]
    return r
