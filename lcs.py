


def lcs(s,t):
    ls = len(s)
    lt = len(t)
    dp = [[0 for _ in range(lt+1)] for _ in range(ls+1)]

    for i in range(1,ls+1):
        for j in range(1,lt+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i][j])

    return dp

def reverse_lcs(dp,s,t):
    n = len(dp)
    m = len(dp[0])
    assert len(s) == n - 1
    assert len(t) == m - 1
    y = n - 1
    x = m - 1
    ans = []
    while y > 0 and x > 0:
        if s[y-1] == t[x-1]:
            ans.append(s[y-1])
            y -= 1
            x -= 1
        else:
            if dp[y][x] == dp[y][x-1]:
                x -= 1
            else:
                y -= 1
    return "".join(reversed(ans))




def main():
    s = input()
    t = input()
    dp = lcs(s,t)
    ans = reverse_lcs(dp,s,t)
    print(ans)

main()