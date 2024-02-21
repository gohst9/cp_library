
class BIT:

    def __init__(self,lst):
        self.n = len(lst) + 1
        self.bit = [0 for _ in range(self.n)]

        for i in range(1,self.n):
            self.add(i-1,lst[i-1])


    def right_end(self,x):
        return x & -x

    def add(self,i,x):
        i+=1
        while i < self.n:
            self.bit[i] += x
            i += self.right_end(i)

    def query(self,i):
        ans = 0
        while i > 0:
            ans += self.bit[i]
            i -= self.right_end(i)
        return ans

    def range_sum(self,l,r):
        return self.query(r) - self.query(l)




def main():
    #オブジェクト内では1-indexedだが、クエリは0-indexedで行う
    #右端を含まない半開区間
    lst = [1,2,3,4]
    bit = BIT(lst)

    ans = bit.range_sum(1,3)
    print(ans)
if __name__ == '__main__':
    main()
