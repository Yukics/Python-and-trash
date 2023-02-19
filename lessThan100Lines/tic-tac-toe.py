from random import randrange

def display_board(board):
    separator = " +-------+-------+-------+"
    space = "|   {}   |   {}   |   {}   |"

    for i in range(0, 3):
        print(separator, "\n",
              space.format(" ", " ", " "), "\n",
              space.format(board[i][0], board[i][1], board[i][2]), "\n",
              space.format(" ", " ", " "))
    print(separator)

def player_turn(board, xo):
    player = True

    while player == True:
        casilla = input("Insert your play: ")
        new_board = check_casilla(casilla, board, xo)

        if new_board:
            board = new_board
            player = False

    return board

def ia_turn(board, ox):
    ia = True

    while ia == True:
        casilla = str(randrange(9))
        new_board = check_casilla(casilla, board, ox)

        if new_board:
            board = new_board
            ia = False

    return board

def check_winner(board):

    # Check in line wins
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return True

    # Check diagonal wins
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

    return False

def check_casilla(casilla, board, xo):
    for line in range(0, 3):
        for element in range(0, 3):
            if casilla == board[line][element]:
                board[line][element] = xo
                return board
    return False


if __name__ == "__main__":
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    xo = "X"
    ox = "O"
    # TODO random start
    while True:
        display_board(board)

        board = player_turn(board, xo)
        if check_winner(board):
            print("Player has won")
            break

        board = ia_turn(board, ox)
        if check_winner(board):
            print("AI has won")
            break
