import pygame
from chess_functions import *


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


if __name__ == '__main__':
    main()
