class Ruisekiwa:
    def __init__(self,lst):
        self.lst_a = [0] + lst
        self.lst_sum = self.create_sum(self.lst_a)

    def create_sum(self,lst_a):
        lst_sum = [0] * len(lst_a)
        for a in range(len(lst_a)):
            if a == 0:
                lst_sum[a] = 0
                continue
            lst_sum[a] = lst_sum[a-1] + lst_a[a]
        return lst_sum

    def query(self,l,r):
        if l > r:
            return 0 #クエリの範囲が交差する場合
        return self.lst_sum[r] - self.lst_sum[l-1]



if __name__ == "__main__":
    lst = [10,9,8,7,6,5,4,3,2,1]
    r_lst = Ruisekiwa(lst)
    print(r_lst.lst_a)
    print(r_lst.lst_sum)
    r = 3
    l=5
    print(r,"~",l,"=",r_lst.query(r,l))


