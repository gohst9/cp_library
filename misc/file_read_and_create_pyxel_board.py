import pyxel

goal_color = 6
start_color = 9

#input.txtファイルを読み込み、pyxelで迷路を作る
#input.txtファイルは"#"が壁、"."が床で示されたテキストファイル
#例
# .#.
# #..
# ..#

class App:
    def __init__(self,file_name="input.txt",sx=0,sy=0,gx=1,gy=1,s_width=4,s_height=4):
        self.sx = sx
        self.sy = sy
        self.gx = gx
        self.gy = gy
        self.x = sx
        self.y = sy
        self.s_width = s_width
        self.s_height = s_height
        with open(file_name,"r") as f:
            #self.sx,self.sy = f.readline().split()
            #self.gx,self.gy = f.readline().split()
            self.board = []
            for line in f:
                self.board.append(list(line.strip()))
            self.board_width = max([len(line) for line in self.board])
            self.board_height = len(self.board)

            pyxel.init(self.board_width * self.s_width,self.board_height * self.s_height)

        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        dx = pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)
        dy = pyxel.btn(pyxel.KEY_S) - pyxel.btn(pyxel.KEY_W)
        if pyxel.frame_count %3 == 0:
            nxt_x = self.x + dx
            nxt_y = self.y + dy
            nxt_col = nxt_x // self.s_width
            nxt_row = nxt_y // self.s_height
            if (0 <= nxt_col < self.board_width) and (0 <= nxt_row < self.board_height) and self.board[nxt_row][nxt_col] == ".":
                self.x = nxt_x
                self.y = nxt_y

    def draw(self):
        pyxel.cls(0)
        print(self.board_width)
        print(self.board_height)
        for y in range(self.board_height):
            for x in range(self.board_width):
                color = 1 if self.board[y][x] == "#" else 0
                if x == self.gx and y == self.gy:
                    color = goal_color
                if x == self.sx and y == self.sy:
                    color = start_color
                pyxel.rect(x*self.s_width,y*self.s_height,self.s_width,self.s_height,color)

        pyxel.rect(self.x,self.y,1,1,5)




def main():
    app = App(sx=0,sy=0,gx=2,gy=2)


if __name__ == '__main__':
    main()
