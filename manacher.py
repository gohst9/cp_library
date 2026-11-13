
#参考URL
#https://cympfh.cc/procon/string.manacher.html

import unittest

def manacher(s):
    n = len(s)
    r = [0 for _ in range(2*n-1)]
    i = 0
    j = 0

    while i < 2 * n - 1:
        while i >= j and i+j+1 < 2 * n and s[(i-j)//2] == s[(i+j+1)//2]:
            j += 1
        r[i] = j
        k = 1
        while i + k < 2 * n - 1 and i >= k and r[i] >= k and r[i-k] != r[i]-k:
            r[i+1] = min(r[i-k],r[i]-k)
            k += 1
        i += k
        j = j - k if j > k else 0

    return r



#返り値の配列rはどの文字を中心にするか？　で、0文字目、0と1文字目の間、1文字目、1文字目と2文字目の間
#って感じになる





class Test(unittest.TestCase):


    def test1(self):
        s = "a"
        ans = manacher(s)
        exp = [1]
        self.assertEqual(ans,exp)

    def test2(self):
        s = "aaa"
        ans = manacher(s)
        exp = [1,2,3,2,1]
        self.assertEqual(ans,exp)

    def test3(self):
        s = "aba"
        ans = manacher(s)
        exp = [1,0,3,0,1]
        self.assertEqual(ans,exp)


    def test4(self):
        s = "abcd"
        ans = manacher(s)
        exp = [1,0,1,0,1,0,1]
        self.assertEqual(ans,exp)


    def test5(self):
        s = "abbc"
        ans = manacher(s)
        exp = [1,0,1,2,1,0,1]
unittest.main()