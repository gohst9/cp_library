class SegTree:

    def __init__(self,n=-1,lst=[],func=lambda a,b:a+b,e=0):
        self.func = func
        self.e = e
        x = 1
        if n == -1:
            n = len(lst)
        while x < n:
            x *= 2
        self.n = x
        self.seg = [e] * (self.n * 2)
        for i,v in enumerate(lst):
            self.update(i,v)


    def update(self,i,x):
        i += self.n - 1
        self.seg[i] = x
        while i > 0:
            i = (i-1)//2
            self.seg[i] = self.func(self.seg[i*2+1],self.seg[i*2+2])

    def query(self,l,r):
        assert l <= r
        l += self.n -1
        r += self.n -1
        ans = self.e
        while (l<r):
            if not l&1:
                ans  = self.func(ans,self.seg[l])
                l+=1
            if not r&1:
                ans = self.func(ans,self.seg[r-1])
            l = (l-1)//2
            r = (r-1)//2
        return ans

    def sub_query(self,a,b,k,l,r):
        if b <= l or a >= r: #範囲外
            return self.e
        elif a <= l and r <= b:#すべて範囲内
            return self.seg[k]
        else:
            l_ans = self.sub_query(a,b,k*2+1,l,(l+r)//2)
            r_ans = self.sub_query(a,b,k*2+2,(l+r)//2,r)
            return self.func(l_ans,r_ans)