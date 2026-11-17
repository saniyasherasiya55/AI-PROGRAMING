def display(board):

    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(board, player):

    win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win:

        if board[a] == player and \
           board[b] == player and \
           board[c] == player:

            return True

    return False


def computer_move(board):

    # Try to win
    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            if winner(board, 'O'):

                board[i] = ' '

                return i

            board[i] = ' '

    # Block player
    for i in range(9):

        if board[i] == ' ':

            board[i] = 'X'

            if winner(board, 'X'):

                board[i] = ' '

                return i

            board[i] = ' '

    # Take center
    if board[4] == ' ':
        return 4

    # Take corner
    for i in [0, 2, 6, 8]:

        if board[i] == ' ':
            return i

    # Take any position
    for i in range(9):

        if board[i] == ' ':
            return i


board = [' '] * 9

print("TIC-TAC-TOE")
print("Player = X")
print("Computer = O")

while True:

    display(board)

    position = int(input("Enter position 1-9: ")) - 1

    if position < 0 or position > 8:
        print("Invalid position")
        continue

    if board[position] != ' ':
        print("Position already used")
        continue

    board[position] = 'X'

    if winner(board, 'X'):

        display(board)
        print("Player Wins")
        break

    if ' ' not in board:

        display(board)
        print("Draw")
        break

    move = computer_move(board)

    board[move] = 'O'

    print("Computer selected:", move + 1)

    if winner(board, 'O'):

        display(board)
        print("Computer Wins")
        break

    if ' ' not in board:

        display(board)
        print("Draw")
        break
