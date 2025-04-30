

class Trie:
    def __init__(self):
        self.nxt = dict()
    
    def add(self,s,i=0):
        n = len(s)
        if i == n:
            return
        
        nxt_c = s[i]
        if nxt_c not in self.nxt:
            self.nxt[nxt_c] = Trie()
        self.nxt[nxt_c].add(s,i+1)



    def check(self,s,i=0):
        n = len(s)
        if i == n:
            return True
        nxt_c = s[i]
        if nxt_c not in self.nxt:
            return False
        return self.nxt[nxt_c].check(s,i+1)


def main():
    tri = Trie()
    qn = int(input())
    for _ in range(qn):
        q = input()
        qt,s = q.split()
        if qt == "1":
            tri.add(s)
        if qt == "2":
            print(tri.check(s))

main()

