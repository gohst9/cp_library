#bingo_checker

def is_bingo(lst,mark="#"):
    for c in lst:
        if c != mark:
            return False

    return True


def check_bingo(board):
    h = len(board)
    w = len(board[0])
    assert h == w

    for i in range(h):
        if is_bingo(board[i]):
            return True
        if is_bingo([board[j][i] for j in range(h)]):
            return True

    dx = 1
    dy = 1
    x = 0
    y = 0
    if is_bingo([board[i][i] for i in range(h)]):
        return True
    if is_bingo([board[i][h-1-i] for i in range(h)]):
        return True

    return False
