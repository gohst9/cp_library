from bisect import bisect_left

#最長増加部分列
#dpっテーブルを作って返却

def lis(lst,INF = 10**100):
    n = len(lst)
    dp = [INF for _ in range(n+1)]

    for i in range(n):
        x = lst[i]
        idx = bisect_left(dp,x)
        dp[idx] = x
    
    return dp



def main():
    a = list(map(int,input().split()))

    INF = 10**100
    dp = lis(a,INF)


    for i in range(len(a)):
        if dp[i] == INF:
            break

    print(i)

main()
