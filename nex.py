
class Nex:
    def __init__(self,tgt_s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s = tgt_s.lower()
        n = len(s)
        self.n = n
        self.lst = [{c:n for c in alphabet} for _ in range(n + 1)]

        for i in range(n-1,-1,-1):
            for c in alphabet:
                self.lst[i][c] = self.lst[i+1][c]
            self.lst[i][s[i]] = i
    def __getitem__(self,key):
        return self.lst[key]

    def get(self,i,c):
        return self.lst[i][c]

    def is_exist(self,i,c):
        return self.lst[i][c] != self.n