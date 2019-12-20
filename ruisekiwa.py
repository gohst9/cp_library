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
            lst_sum[a] = lst_sum[a-1] + a
        return lst_sum
            
    def query(self,l,r):
        return self.lst_sum[r] - self.lst_sum[l-1]



if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9,10]
    r_lst = Ruisekiwa(lst)
    print(r_lst.lst_a)
    print(r_lst.lst_sum)
    print("4,7=",r_lst.query(4,7))

        