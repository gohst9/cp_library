class Tree:

    def __init__(self,ide,lst,func):
        self.ide = ide
        self.func = func
        self.n = len(lst)
        self.offset = 1 << (self.n-1).bit_length()
        self.tree = [self.ide] * (self.offset*2)
        self.lazy = [None] * (self.offset*2)


        for i in range(self.n):
            self.tree[self.offset + i] = lst[i]
        
        for i in range(self.offset-1,0,-1):
            self.tree[i] = self.func(self.tree[i*2],self.tree[i*2+1])

    def gindex(self,l,r):
        l += self.offset
        r += self.offset
        lm = (l // (l & -l)) >> 1
        rm = (r // (r & -r)) >> 1

        while l < r:
            if r <= rm:
                yield r
            if l <= lm:
                yield l
            l >>= 1
            r >>= 1
        while l:
            yield l
            l >>= 1
    
    def propagates(self,i):
        nxt = self.lazy[i]
        if nxt is None:
            return
        self.lazy[i] = None
        self.lazy[2*i] = nxt
        self.lazy[2*i+1] = nxt
        self.tree[2*i] = nxt
        self.tree[2*i+1] = nxt

    def update(self,l,r,value):

        
        idxs = list(self.gindex(l,r))
        for i in reversed(idxs):
            self.propagates(i)
        l += self.offset
        r += self.offset


        while l < r:
            if r & 1:
                self.lazy[r-1] = value
                self.tree[r-1] = value
                r -= 1
            
            if l & 1:
                self.lazy[l] = value
                self.tree[l] = value
                l += 1
            l >>= 1
            r >>= 1

        for i in idxs:
            self.tree[i] = self.func(self.tree[2*i],self.tree[2*i+1])

    def query(self,l,r):
        for i in reversed(list(self.gindex(l,r))):
            self.propagates(i)
        l = self.offset + l
        r = self.offset + r

        left_ans = self.ide
        right_ans = self.ide

        while l < r:
            if l & 1: #lが右側の子
                left_ans = self.func(left_ans,self.tree[l])
                l += 1
            
            if r & 1: #rが左の子
                right_ans = self.func(right_ans,self.tree[r-1])
            
            l //= 2
            r //= 2
        return self.func(left_ans,right_ans)

def main():
    n,q = map(int,input().split())
    INF = 2**31-1
    tree = Tree(INF,[INF]*n,min)
    for _ in range(q):
        t,*values = map(int,input().split())

        if t == 0:
            s,t,x = values
            tree.update(s,t+1,x)
        else:
            s,t = values
            print(tree.query(s,t+1))

main()
# verify https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=9628947#2