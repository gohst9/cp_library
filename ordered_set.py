from random import randint
MAX_HEIGHT = 1 << 6

class Skip_node:
    def __init__(self,value,height):
        self.value = value
        self.height = height
        #self.nxt 各高さにおける現在のノードの次にある要素。連結リストなので繋ぎ変えや削除が容易
        #Noneで初期化されているけど、もし存在するならSkip_nodeが入る
        self.nxt = [None for _ in range(self.height + 1)]


class Skip_lst:
    def __init__(self,lst = []):
        #番兵　一番上の左端から探索を開始する
        self.sentinel = Skip_node(None,MAX_HEIGHT)
        self.height = 0 #addするときに最大高さが変化するなら更新
        self.length = 0 #addやremoveするたびに変化
        if len(lst) >= 1:
            for item in lst:
                self.add(item)

    def __len__(self):
        return self.length

    def find(self,tgt_value):
        here = self.sentinel #一番上の左端から探索開始

        for h in range(self.height,-1,-1):
            #現在注目しているノードがNoneでないかチェックしつつ、目標の値にできるだけ近づくよう右に進む
            #目標値に近づくようwhileでできるだけ進む。forループが1周すると下への移動。
            while here.nxt[h] != None and here.nxt[h].value <= tgt_value:
                here = here.nxt[h]

            if here.value == tgt_value:
                return tgt_value
        return None




    def pick_height(self):
        #コイントスをして各要素の「高さ」を決める
        #元のコードでは2進数を作っていたが、0,1の乱数を作ればいいのでrandint(0,1)でやってる
        h = 0
        while h <= MAX_HEIGHT:
            coin = randint(0,1)
            if coin == 0:
                break
            h += 1
        return h

    def add(self,new_value):
        here = self.sentinel
        #このスタックは「新たに追加した要素の左側のノード」がまとめて入る
        #なぜわざわざスタックにするのか？　もし重複する要素を入れた場合、
        #集合なので操作をキャンセルしなくてはいけないため。挿入が確定した後にまとめて操作できるよう
        #スタックになっている
        stack = [self.sentinel for _ in range(MAX_HEIGHT)]
        for h in range(self.height,-1,-1):
            while here.nxt[h] is not None and here.nxt[h].value <= new_value:
                here = here.nxt[h]
            #重複した要素を挿入しようとした場合キャンセルして早期リターン
            if here.value == new_value:
                return
            stack[h] = here
        new_node = Skip_node(new_value,self.pick_height())

        if new_node.height > self.height:
            self.height = new_node.height
        for h in range(new_node.height+1):
            new_node.nxt[h] = stack[h].nxt[h]
            stack[h].nxt[h] = new_node
        self.length += 1

    def remove(self,tgt_value):
        here = self.sentinel
        removed = False
        for h in range(self.height,-1,-1):
            while here.nxt[h] != None and here.nxt[h].value < tgt_value:
                here = here.nxt[h]
            #探索の途中で繋ぎ変え
            if here.nxt[h] != None and here.nxt[h].value == tgt_value:
                removed = True
                here.nxt[h] = here.nxt[h].nxt[h]
                if here.value == None and here.nxt[h] == None:
                    self.height -= 1
        if removed:
            self.length -= 1

    def upper(self,tgt_value):
        here = self.sentinel
        for h in range(self.height,-1,-1):
            while here.nxt[h] != None and here.nxt[h].value < tgt_value:
                here = here.nxt[h]

        return here.nxt[0].value if here.nxt[0] != None else None

    def lower(self,tgt_value):
        here = self.sentinel
        for h in range(self.height,-1,-1):
            while here.nxt[h] != None and here.nxt[h].value <= tgt_value:
                here = here.nxt[h]

        return here.value

def main():
    pass

if __name__ == '__main__':
    main()
