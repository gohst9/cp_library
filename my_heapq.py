
class heapq:
    def __init__(self,lst):
        self.lst = []
        for i in range(len(lst)):
            self.push(lst[i])

    def push(self,value):
        self.lst.append(value)
        if len(self.lst) == 1:
            return
        here = len(self.lst) - 1
        while True:
            parent = self.find_parent(here)
            if parent == None:
                break
            if self.lst[parent] > self.lst[here]:
                self.lst[parent],self.lst[here] = self.lst[here],self.lst[parent]
                here = parent
            else:
                break



    def pop(self):
        rtn = self.lst[0]
        self.lst[0] = self.lst[-1]
        self.lst.pop()
        here = 0
        while True:
            left_child = self.find_left_child(here)
            right_child = self.find_right_child(here)
            if left_child == None and right_child == None:
                break
            if right_child == None:
                child = left_child
            else:
                child = left_child if self.lst[left_child] < self.lst[right_child] else right_child

            if self.lst[here] > self.lst[child]:
                self.lst[here],self.lst[child] = self.lst[child],self.lst[here]
                here = child
                continue
            else:
                break
        return rtn

    def find_left_child(self,i):
        child_index = i * 2 + 1
        if child_index >= len(self.lst):
            return None
        return child_index


    def find_right_child(self,i):
        child_index = i * 2 + 2
        if child_index >= len(self.lst):
            return None
        return child_index


    def find_parent(self,i):
        if i == 0:
            return None
        return (i-1) // 2


