class Ruisekiwa:
    def __init__(self,lst):
        s = 0
        self.r = [0]
        for i,_ in enumerate(lst):
            self.r.append(s+lst[i])
            s += lst[i]

    def query(self,a,b):
        #リスト内の半開区間[a,b)の総和
        return self.r[b] - self.r[a]

def main():
    pass

##def ruisekiwa(l):
##    #関数バージョン
##    lst = [0]
##    s = 0
##    for i,v in enumerate(l):
##        lst.append(s + v)
##        s += v
##    return lst



if __name__ == '__main__':
    main()
