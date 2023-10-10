#リストaの中から合計がkを越えない最長の連続部分裂の長さを求める


def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))


    temp = 0
    r = 0
    mx = -1
    for l in range(n):
        if r < l:
            temp = 0
            r = l

        while True:
            if r >= n:
                break
            if temp + a[r] <= k:
                mx = max(mx,r-l+1)
            if r+1 < n and temp + a[r+1] <= k:
                temp += a[r]
                r += 1
            else:
                break
        temp -= a[l]

    print(mx)


if __name__ == '__main__':
    main()
