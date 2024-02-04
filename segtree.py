class SegTree:

    def __init__(self,lst=[],func=lambda a,b:a+b,e=0):
        self.func = func
        self.e = e
        n = len(lst)
        x = 1
        while x < n:
            x *= 2
        self.n = x
        self.seg = [e] * (self.n * 2)
        for i,v in enumerate(lst):
            self.update(i,v)




    def update(self,i,x):
        i += self.n-1
        self.seg[i] = x
        while i > 0:
            i = (i-1)//2
            self.seg[i] = self.func(self.seg[i*2+1],self.seg[i*2+2])

    def query(self,a,b):
        assert a <= b
        return self.sub_query(a,b,0,0,self.n)

    def sub_query(self,a,b,k,l,r):
        if b <= l or a >= r: #範囲外
            return self.e
        elif a <= l and r <= b:#すべて範囲内
            return self.seg[k]
        else:
            l_ans = self.sub_query(a,b,k*2+1,l,(l+r)//2)
            r_ans = self.sub_query(a,b,k*2+2,(l+r)//2,r)
            return self.func(l_ans,r_ans)

def main():
    lst = [1,2,3,4,5,6,7,8]
    seg = SegTree(lst,func=max)
    ans = seg.query(0,3)
    print(ans)
    seg.update(5,5)
    ans = seg.query(4,5)
    print(ans)

if __name__ == '__main__':
    main()
