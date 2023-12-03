import unittest

def cul_s(board):
    h = len(board)
    w = len(board[0])

    s = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for y in range(h):
        for x in range(w):
            s[y+1][x+1] = s[y][x+1] + s[y+1][x] - s[y][x] + board[y][x]

    return s

def get_sum(y1,x1,y2,x2,s):
    total = s[y2+1][x2+1] - s[y1][x2+1] - s[y2+1][x1] + s[y1][x1]
    return total

def get_sum2(y,x,s):
    #(0,0)からの総面積だけ求めればいいとき用
    total = s[y+1][x+1]
    return total

def main():
    h,w = map(int,input().split())
    board = []
    for _ in range(h):
        board.append(list(map(int,input().split())))
    s = cul_s(board)
    for line in s:
        print(*line)


class Test(unittest.TestCase):
    def test_1(self):
        board = [[1,1,1],
                 [1,1,1],
                 [1,1,1],]
        s = cul_s(board)
        answer = get_sum(0,0,2,2,s)
        expected = 9
        self.assertEqual(expected,answer)

    def test_2(self):
        board = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        s = cul_s(board)
        answer = get_sum(1,1,2,2,s)
        expected = 28
        self.assertEqual(expected,answer)

    def test_3(self):
        board = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        s = cul_s(board)
        answer = get_sum(0,0,1,2,s)
        expected = 21
        self.assertEqual(expected,answer)

    def test_4(self):
        board = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        s = cul_s(board)
        answer = get_sum2(2,2,s)
        expected = 45
        self.assertEqual(expected,answer)

if __name__ == '__main__':
    unittest.main()
