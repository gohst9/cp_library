import unittest


def get_line(x1,y1,x2,y2):
    katamuki = (y2-y1)/(x2-x1)
    seppen = y1 - katamuki*x1
    return katamuki,seppen

def line_cross_point(a,b,c,d):
    #a直線1の傾き c直線2の傾き
    #b直線2の切片 c直線dの傾き
    if a == c:
        return 
    x = (d-b)/(a-c)
    y = (a*d-b*c)/(a-c)
    return (x,y)
class Test(unittest.TestCase):

    def test_solve1(self):
        x1,y1 = 3,1
        x2,y2 = 4,3
        katamuki,seppen = get_line(x1,y1,x2,y2)
        self.assertEqual((katamuki,seppen) , (2,-5))

ans = line_cross_point(1,0,2,-1)
print(ans)
#unittest.main()

