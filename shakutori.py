class Shakutori:
    def __init__(self,lst,mono=0,limit=0):
        self.lst = lst
        self.mono = mono
        self.limit = limit
        self.answer = self.mono

    def calc(self):
        l = 0
        r = 1
        while l <= len(self.lst) and r < len(self.lst):
            if self.judge(self.lst[l:r]):
                self.answer_update()
                print(self.lst[l:r])

            #ここの尺取らせ方が間違ってるからちゃんと考えようね！
            if (self.judge(self.lst[l:r]) and r < len(self.lst)) or l >= r-1:
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


lst = [1,2,3,4,5,6,7,8,9]
s = Shakutori(lst,0,5)
print(s.calc())

