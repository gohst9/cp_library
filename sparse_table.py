
class Sparse_table:

    def __init__(self,lst,func=min):
        self.func = func
        self.lst = lst
        self.n = len(lst)
        self.log_table = self.create_log_table()
        self.table = self.create_table()

    def create_log_table(self):
        log_table = [0] * (self.n+1)
        for i in range(2,self.n+1):
            log_table[i] = log_table[i>>1] + 1
        return log_table


    def create_table(self):
        table = [[-1 for _ in range(self.log_table[self.n]+1)] for _ in range(self.n)]

        for i in range(self.n):
            table[i][0] = i

        for k in range(1,self.log_table[self.n]+1):
            for i in range(self.n):
                if i + (1 << k) > self.n:
                    break
                ind1 = table[i][k-1]
                ind2 = table[i+(1 << (k-1))][k-1]
                if self.func(self.lst[ind1],self.lst[ind2]) == self.lst[ind1]:
                    table[i][k] = ind1
                else:
                    table[i][k] = ind2
##                if self.lst[ind1] < self.lst[ind2]:
##                    table[i][k] = ind1
##                else:
##                    table[i][k] = ind2
        return table

    def query(self,l,r):
        k = self.log_table[r-l]
        ind1 = self.table[l][k]
        ind2 = self.table[r-(1 << k)][k]
        return self.func(self.lst[ind1],self.lst[ind2])


def main():
    lst = [2,3,5,10,3,7,10,3,4,5,3,8,9,2,3]
    s = Sparse_table(lst,max)
    print(s.log_table)
    print(s.table)
    print(s.query(0,3))

if __name__ == '__main__':
    main()
