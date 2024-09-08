
import unittest

class Tree:

    def __init__(self,ide,lst,func):
        self.ide = ide
        self.func = func
        self.n = len(lst)
        self.offset = 1 << (self.n-1).bit_length()
        self.tree = [self.ide] * (self.offset*2)


        for i in range(self.n):
            self.tree[self.offset + i] = lst[i]
        
        for i in range(self.offset-1,0,-1):
            self.tree[i] = self.func(self.tree[i*2],self.tree[i*2+1])
    

    def update(self,idx,value):
        idx += self.offset
        self.tree[idx] = value

        while idx > 1:
            parent = idx//2
            self.tree[parent] = self.func(self.tree[parent*2],self.tree[parent*2+1])

            idx = idx//2


    def query(self,l,r):
        left_ans = self.ide
        right_ans = self.ide
        l += self.offset
        r += self.offset

        while l < r:
            if l & 1: #lが右側の子
                left_ans = self.func(left_ans,self.tree[l])
                l += 1
            
            if r & 1: #rが左の子
                right_ans = self.func(right_ans,self.tree[r-1])
                r -= 1
            
            l //= 2
            r //= 2
        return self.func(left_ans,right_ans)




def main():
    lst = [6,2,3,5]
    func = lambda a,b:a+b
    tree = Tree(0,lst,func)
    ans = tree.query(0,4)
    print(ans)

main()