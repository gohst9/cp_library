

class Csum_2d:
    def __init__(self,board):
        h = len(board)
        w = len(board[0])
        csum = [[0 for _ in range(w+1)] for _ in range(h+1)]

        for y in range(h):
            for x in range(w):
                csum[y+1][x+1] = csum[y+1][x] + csum[y][x+1] - csum[y][x] + board[y][x]

        self.csum = csum

    def query(self,y1,x1,y2,x2):
        #0-indexedの半開区間
        return self.csum[y2][x2] - self.csum[y1][x2] - self.csum[y2][x1] + self.csum[y1][x1]


