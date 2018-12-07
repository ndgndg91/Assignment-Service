import pygame


def main():
    explicate_input()  # Provide instructions to the user for using your program
    chess_board = get_inputs()  # Provide a way for the user to type in the current state of a chessboard
    print_chess_board(chess_board)  # print current chess board
    for_draw = convert_list(chess_board)  # A function to convert list to draw chess board
    pieces = piece_info(chess_board)  # A function to find out what pieces are needed to draw a chessboard
    draw_board(for_draw, pieces)  # show current chess board to user using pygame library
    while True:
        choice = ask_options()
        if choice == 3:  # Quit and  Calculate the score associated with each player and report which player is winning
            white_score = sum_white(chess_board)
            black_score = sum_black(chess_board)
            which_win(white_score, black_score)
            break
        elif choice == 1:
            explicate_input()  # Provide instructions to the user for using your program
            chess_board = get_inputs()  # Provide a way for the user to type in the current state of a chessboard
            print_chess_board(chess_board)  # print current chess board
            for_draw = convert_list(chess_board)  # A function to convert list to draw chess board
            pieces = piece_info(chess_board)  # A function to find out what pieces are needed to draw a chessboard
            draw_board(for_draw, pieces)  # show current chess board to user using pygame library
        elif choice == 2:
            print_chess_board(chess_board)
            for_draw = convert_list(chess_board)
            pieces = piece_info(chess_board)
            draw_board(for_draw, pieces)
            chess_board = move(chess_board)
            print_chess_board(chess_board)
            for_draw = convert_list(chess_board)
            pieces = piece_info(chess_board)
            draw_board(for_draw, pieces)
        print()


def draw_board(the_board, pieces):  # show current chess board to user using pygame library
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255, 255, 255), (0, 0, 0)]  # Set up colors [red, black]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    surface_sz = n * sq_sz  # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    w_queen = pygame.image.load("w_queen.jpg")
    w_king = pygame.image.load("w_king.jpg")
    w_knight = pygame.image.load("w_knight.jpg")
    w_rook = pygame.image.load("w_rook.jpg")
    w_bishop = pygame.image.load("w_bishop.jpg")
    w_pawn = pygame.image.load("w_pawn.jpg")

    b_queen = pygame.image.load("b_queen.jpg")
    b_king = pygame.image.load("b_king.jpg")
    b_knight = pygame.image.load("b_knight.jpg")
    b_rook = pygame.image.load("b_rook.jpg")
    b_bishop = pygame.image.load("b_bishop.jpg")
    b_pawn = pygame.image.load("b_pawn.jpg")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    w_queen_offset = (sq_sz - w_queen.get_width()) // 2
    w_king_offset = (sq_sz - w_king.get_width()) // 2
    w_knight_offset = (sq_sz - w_knight.get_width()) // 2
    w_rook_offset = (sq_sz - w_rook.get_width()) // 2
    w_bishop_offset = (sq_sz - w_bishop.get_width()) // 2
    w_pawn_offset = (sq_sz - w_pawn.get_width()) // 2

    b_queen_offset = (sq_sz - b_queen.get_width()) // 2
    b_king_offset = (sq_sz - b_king.get_width()) // 2
    b_knight_offset = (sq_sz - b_knight.get_width()) // 2
    b_rook_offset = (sq_sz - b_rook.get_width()) // 2
    b_bishop_offset = (sq_sz - b_bishop.get_width()) // 2
    b_pawn_offset = (sq_sz - b_pawn.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_index = row % 2  # Alternate starting color
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_index], the_square)
                # Now flip the color index for the next square
                c_index = (c_index + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (row, col) in enumerate(the_board):
            if col == 8:
                continue
            else:
                if pieces[row] == 'q':
                    surface.blit(w_queen,
                                 (col * sq_sz + w_queen_offset, row * sq_sz + w_queen_offset))
                elif pieces[row] == 'k':
                    surface.blit(w_king,
                                 (col * sq_sz + w_king_offset, row * sq_sz + w_king_offset))
                elif pieces[row] == 'b':
                    surface.blit(w_bishop,
                                 (col * sq_sz + w_bishop_offset, row * sq_sz + w_bishop_offset))
                elif pieces[row] == 'n':
                    surface.blit(w_knight,
                                 (col * sq_sz + w_knight_offset, row * sq_sz + w_knight_offset))
                elif pieces[row] == 'r':
                    surface.blit(w_rook,
                                 (col * sq_sz + w_rook_offset, row * sq_sz + w_rook_offset))
                elif pieces[row] == 'p':
                    surface.blit(w_pawn,
                                 (col * sq_sz + w_pawn_offset, row * sq_sz + w_pawn_offset))
                elif pieces[row] == 'Q':
                    surface.blit(b_queen,
                                 (col * sq_sz + b_queen_offset, row * sq_sz + b_queen_offset))
                elif pieces[row] == 'K':
                    surface.blit(b_king,
                                 (col * sq_sz + b_king_offset, row * sq_sz + b_king_offset))
                elif pieces[row] == 'B':
                    surface.blit(b_bishop,
                                 (col * sq_sz + b_bishop_offset, row * sq_sz + b_bishop_offset))
                elif pieces[row] == 'R':
                    surface.blit(b_rook,
                                 (col * sq_sz + b_rook_offset, row * sq_sz + b_rook_offset))
                elif pieces[row] == 'P':
                    surface.blit(b_pawn,
                                 (col * sq_sz + b_pawn_offset, row * sq_sz + b_pawn_offset))
                elif pieces[row] == 'N':
                    surface.blit(b_knight,
                                 (col * sq_sz + b_knight_offset, row * sq_sz + b_king_offset))

        pygame.display.flip()

    pygame.quit()


def old_location(some_list):  # 옮길 말을 입력받는 함수
    r = []
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col = [1, 2, 3, 4, 5, 6, 7, 8]
    show_requirement()
    while True:
        o_row = input('enter the row :')
        o_col = int(input('enter the column :'))
        if o_row in row and o_col in col:
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
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col = [1, 2, 3, 4, 5, 6, 7, 8]
    show_requirement('of the piece')
    while True:
        n_row = input('enter the row :')
        n_col = int(input('enter the column :'))
        if n_row in row and n_col in col:
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


if __name__ == '__main__':
    main()
