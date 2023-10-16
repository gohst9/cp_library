

def sequence_check(lst,start=0,check=lambda a,b:a==b,only_length=False):
    #check: 　「連続しているか」を判定する関数。デフォルトだと同じ値
    #only_lengths:　シークエンスの長さだけを返す
    temp = lst[start]
    length = 1
    answer = []
    for i in range(start,len(lst)):
        if i+1 >= len(lst):
            answer.append((temp,length))
            break
        if not check(temp,lst[i+1]):
            answer.append((temp,length))
            temp = lst[i+1]
            length = 1
            continue
        temp = lst[i+1]
        length += 1
    if only_length:
        return [ans[1] for ans in answer]
    return answer


import unittest
class Test(unittest.TestCase):
    def test_1(self):
        lst = [1,1,1,2,2,2]
        expected = sequence_check(lst)
        self.assertEqual(expected,[(1,3),(2,3)])

    def test_2(self):
        lst = [1,2,3,2,3]
        expected = sequence_check(lst,check=lambda a,b:a <= b,only_length=True)
        self.assertEqual(expected,[3,2])

    def test_3(self):
        lst = [1,2,3]
        expected = sequence_check(lst)
        self.assertEqual(expected,[(1,1),(2,1),(3,1)])

    def test_4(self):
        lst = [0]
        expected = sequence_check(lst)
        self.assertEqual(expected,[(0,1)])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
