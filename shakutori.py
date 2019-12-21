class Shakutori:
    def __init__(self,lst,mono=0,limit=0):
        self.lst = lst
        self.mono = mono
        self.limit = limit
        self.answer = self.mono

    def calc(self):
        l = 0
        r = 1
        while l <= len(self.lst) and r < len(self.lst)+1:
            if self.judge(self.lst[l:r]):
                self.answer_update()
                print(self.lst[l:r])

            #rを+1したとき条件に合うか判定。合えばr+=1 合わない、合わないならl+=1
            if  (r <= len(self.lst)+1 and self.judge(self.lst[l:r+1])) or l >= r-1:
                r += 1
            else:
                l += 1



        return self.answer



    def judge(self,lst):
        if sum(lst) <= self.limit:
            return True
        else:
            return False

    def answer_update(self):
        self.answer += 1


lst = [1,2,3,4,5,6,7,2,3]
s = Shakutori(lst,0,5)
print(s.calc())

