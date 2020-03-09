#import sys
#sys.setrecursionlimit(500000)　マージテクをちゃんとしていればこんなものはいらないはず……

class UF:
    #経路圧縮＋マージテクのunion find木
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * (n+1) #1-indexedにするために１個足している
        self.rnks = [0] * (n+1)

    def find(self,n):
        if self.parents[n] < 0:
            return n
        else:
            return self.find(self.parents[n])


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
        if self.size(a_par) < self.size(b_par): #parentsの値が負の数のとき、それはその木のサイズを表す。
            a_par,b_par = b_par,a_par
        self.parents[a_par] += self.parents[b_par]
        self.parents[b_par] = a_par

    def size(self,n):
        par = self.find(n)
        return abs(self.parents[par])

    def is_same(self,a,b):
        return self.find(a) == self.find(b)

