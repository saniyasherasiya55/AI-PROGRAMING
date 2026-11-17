def is_safe(board, row, col, n):

    # Check column
    for i in range(row):

        if board[i] == col:
            return False

    # Check diagonal
    for i in range(row):

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


def print_board(board, n):

    for row in range(n):

        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


n = 4

board = [-1] * n

if solve(board, 0, n):

    print("N-Queens Solution")
    print_board(board, n)

else:

    print("No solution")
