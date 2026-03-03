def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    board = [-1] * n

    def backtrack(row):
        if row == n:
            print(board)
            return True
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                if backtrack(row + 1):
                    return True
        return False

    backtrack(0)

n = int(input("Enter N: "))
solve_nqueens(n)
