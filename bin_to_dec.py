
def dec_to_bin(s):
    #1と0で作られた文字列を受け取り、二進数として計算。10進数にして返す。

    weight = 1 #桁の重み
    total = 0 #

    for c in s[::-1]:
        #print("現在の桁の重み:",weight)
        arrow = " " * (len(s)-1) + "↓"
        print(arrow)
        print(s,"現在の桁の重み:",weight)
        if s[-1] == "1": #現在の数値の末尾の桁に注目。1なら桁の重みを合計に加算。
            total += weight
            print("加算")
        else:
            print("スルー")
        print()


        s = s[:-1] #末尾の桁を切り飛ばす。
        weight *= 2 #2進数なので、桁がひとつ上がると桁の重みは2倍になる

        print("合計:",total)
        print()

    return total


if __name__ == '__main__':
    s = input()
    print(dec_to_bin(s))

