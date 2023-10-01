#二次元グリッドの90度回転
def rotate(lst):
    l = len(lst)
    new_lst = list(zip(*lst[::-1]))
    return new_lst

def show_lst(lst):
    for line in lst:
        print("".join(line))

def main():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(input())
    show_lst(board)
    board = rotate(board)
    show_lst(board)
    board  =rotate(board)
    show_lst(board)
    board = rotate(board)
    show_lst(board)


if __name__ == '__main__':
    main()
