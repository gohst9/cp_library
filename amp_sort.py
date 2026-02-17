from functools import cmp_to_key
#https://atcoder.jp/contests/abc442/tasks/abc442_e
#Laser Takahashiを参考
#通常は反時計周りに使用
#問題によって時計周りに使用するときは逆順に


def cross(a,b):
    #外積
    ax,ay = a
    bx,by = b
    return ax * by - ay * bx
    #正の数なら反時計周り
    #負の数なら時計周り
    #0なら同じ角度
    #数値の大きさは平行四辺形の面積

def cmp(a,b):
    #a (x1,y1)
    #b (x2,y2)
    #X軸を含まず反時計回り
    #Y=0 X > 0 が反時計周りの最初
    #1なら反時計まわり
    #0なら同じ角度
    #-1なら時計まわり
    ax,ay = a
    bx,by = b
    ah = ay < 0 or (ay ==  0 and ax < 0)
    bh = by < 0 or (by == 0 and bx < 0)
    if ah != bh:
        if ah < bh:
            return 1
        else:
            return -1
    
    if ax * by - bx * ay > 0:
        return 1
    elif ax*by - bx*ay == 0:
        return 0
    else:
        return -1




def main(): 
    x1,y1,x2,y2 = map(int,input().split())
    print(cmp((x1,y1),(x2,y2)))

main()