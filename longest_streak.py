def func(s,c1="1",c2="0"):
    """'1'と'0'で構成される文字列の中の
        最も'1'が長く続く部分の長さを求める"""
    left,right = 0,0
    mx = -1
    for c in s:
        if c == "1":
            right += 1
        else:
            mx = max(mx,right-left)
            right += 1
            left = right
    mx = max(mx,right-left)
    return mx

def main():

    s = input()
    print(func(s))

if __name__ == '__main__':
    main()
