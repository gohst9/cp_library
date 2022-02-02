class Sequence:
    #同じ要素が続くまで回り続け、切り替わったタイミングで止まるイテレータ
    def __init__(self,lst,pointer=0,pre=None):
        self.lst = lst
        self.pre = pre
        self.pointer = pointer
        self.length = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_end() or self.pre != self.lst[self.pointer]:
            raise StopIteration()
        ret = self.lst[self.pointer]
        self.pointer += 1
        self.length += 1
        return ret

    def ready(self):
        #一番最初や要素の切り替わりの後に行う。
        self.pre = self.lst[self.pointer]
        self.length = 0

    def get(self):
        #現在見ている連続している要素とその長さを返す。
        return (self.pre,self.length)

    def is_end(self):
        return self.pointer >= len(self.lst)


def main():
    lst = [1,1,1,1,1,0,0,0,0,1,1,1,0,0,0]
    seq = Sequence(lst)
    while not seq.is_end():
        seq.ready()
        for s in seq:
            pass
        print(*seq.get())


if __name__ == '__main__':
    main()
