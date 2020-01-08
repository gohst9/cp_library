#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     08/01/2020
# Copyright:   (c) user 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class UnionFind:
    def __init__(self,value):
        self.value = value
        self.parent  = self
        self.rank = 0
    def union(self,UF):
        #UF別のUnion-Find木
        if self.rank >= UF.rank:
            self.parent = UF
            UF.rank += 1
        else:
            UF.parent = self
            self.rank += 1

    def find(self,lst=[]):
        #lstには探索中根ではなかった要素を入れていき、根が見つけたときに
        #まとめてparentを根要素に付け替える。（経路圧縮）
        if self.parent == self:
            for i in lst:
                i.parent = self
            return self
        else:
            lst.append(self)
            return self.parent.find(lst)
    def isSame(self,UF):

        if self.find() == UF.find():
            return True
        else:
            return False

def main():
    lst = ["taro","jiro","saburo","shiro"]
    lst = list(map(UnionFind,lst))
    befriends = lambda a,b:lst[a].union(lst[b]) #befriends(a,b) aがbの友達になる。
    befriends(0,1)
    befriends(1,2)

    print(lst[1].find())
    print(lst[2].find())
    print(lst[1].isSame(lst[2]))
    if lst[1].isSame(lst[2]):
        print(lst[1].value + "くんは" + lst[2].value + "くんと友達です" )

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i].isSame(lst[j]):
                print(str(i) + lst[i].value + "くんは" + str(j) + lst[j].value + "くんと友達です" )
            else:
                print(str(i) + lst[i].value + "くんは" + str(j) + lst[j].value + "くんと友達じゃないです" )






if __name__ == '__main__':
    main()
