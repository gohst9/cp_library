class Tree:
    def __init__(self,lst,func = lambda a,b:a+b,monoid=0):
        self.func = func
        self.monoid = monoid
        size = len(lst)
        n = 1
        #nを元の配列のサイズ以上になる最小の2べきにする
        while(n < size):
            n *= 2
        self.n = n

        #木構造用リストのを初期化　今は暫定で0を入れているが後にモノイドを受け取るようにする。
        self.seg = [self.monoid] * (2 * n -1)
        for i in range(len(lst)):
            self.seg[i+n-1] = lst[i]

        for i in range(n-1-1, -1 , -1):
            self.seg[i] = self.func(self.seg[2*i+1],self.seg[2*i+2])

        for i in self.seg:
            print(i)
        print()

    def update(self,i,val):
        #もともとのリストでi番目にあたる数をvalに置き換える。
        i += (self.n - 1) #n-1はオフセット。木構造用ツリーの最下段へ。
        self.seg[i] = val
        while i > 0:
            i = (i - 1) // 2
            self.seg[i] = self.func(self.seg[2*i +1],self.seg[2*i+ 2])
        for i in self.seg:
            print(i)



    def query(self,a,b,p=0,l=0,r=-1):
        if r<0:
            r = self.n
        if r <= a or b <= l:
            return self.monoid
        if a <= l and r <= b:
            return self.seg[p]

        #自分の理解力が追い付かなかったので再帰関数で実装している
        #しかしpythonの再帰はドチャクソ遅いという話……
        #いずれはビット演算を使ったメチャ早という噂の実装方法に変えていきたい。

        vl = self.query(a,b,2*p+1,l,(l+r)//2)
        vr = self.query(a,b,2*p+2,(l+r)//2,r)
        return self.func(vl,vr)


t = Tree([1,2,3,4])

print("answer = ",t.query(0,2))
