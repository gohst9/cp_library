#import sys
#sys.setrecursionlimit(500000)　マージテクをちゃんとしていればこんなものはいらないはず……

import unittest

class UF:
    #経路圧縮＋マージテクのunion find木
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * (n+1) #1-indexedにするために１個足している
        self.rnks = [0] * (n+1)
        self.left = [i for i in range(n+1)]
        self.right = [i for i in range(n+1)]

    def find(self,n):
        if self.parents[n] < 0:
            return n
        else:
            par = self.find(self.parents[n])
            self.parents[n] = par
            return par
    
    def get_left(self,n):
        tgt = self.find(n)
        return self.left[tgt]

    def get_right(self,n):
        tgt = self.find(n)
        return self.right[tgt]


    def union(self,a,b):

        a_par = self.find(a)
        b_par = self.find(b)

        if a_par == b_par:
            return
        ##union by rank
        #if self.rnks[a_par] < self.rnks[b_par]: #ランクの高い方の根に低い方の根をつける　逆にしないように……！
        #    a_par,b_par = b_par,a_par
        #if self.rnks[a_par] == self.rnks[b_par]:
        #    self.rnks[a_par] += 1

        a_left = self.get_left(a)
        b_left = self.get_left(b)
        new_left = min(a_left,b_left)
        a_right = self.get_right(a)
        b_right = self.get_right(b)
        new_right = max(a_right,b_right)

        if self.size(a_par) < self.size(b_par): #parentsの値が負の数のとき、それはその木のサイズを表す。
            a_par,b_par = b_par,a_par
        self.parents[a_par] += self.parents[b_par]
        self.parents[b_par] = a_par
        self.left[a_par] = new_left
        self.right[a_par] = new_right

    def range_union(self,a,b):
        if a >= b:
            return
        
        for i in range(a,b):
            self.union(i,i+1)

    def size(self,n):
        par = self.find(n)
        return abs(self.parents[par])

    def is_same(self,a,b):
        return self.find(a) == self.find(b)


class test(unittest.TestCase):

    def test_get_left_or_right(self):
        n = 10
        uf = UF(n)
        uf.union(2,3)
        uf.union(3,4)
        ans = uf.get_left(4) 
        exp = 2
        self.assertEqual(ans,exp)

        ans = uf.get_right(2)
        exp = 4
        self.assertEqual(ans,exp)

    def test_range_union(self):
        n = 10
        uf = UF(n)
        uf.range_union(2,9)
        ans = uf.size(2)
        exp = 8
        self.assertEqual(ans,exp)
unittest.main()
