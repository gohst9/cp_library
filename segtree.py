class Tree:
    def __init__(self,lst,func = lambda a,b:a+b):
        self.func = func
        size = len(lst)
        n = 1
        #nを元の配列のサイズ以上になる最小の2べきにする
        while(n < size):
            n *= 2
        self.seg = [0] * (2 * n -1)
        for i in range(len(lst)):
            self.seg[i+n-1] = lst[i]

        for i in range(n-1-1, -1 , -1):
            self.seg[i] = self.func(self.seg[2*i+1],self.seg[2*i+2])

        for i in self.seg:
            print(i)

    def update(self,i,n):
        pass

    def query(self,a,b):
        pass


t = Tree([1,2,3,4])

