def henshu_kyori(s,t):
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

    for i in range(len(s)+1):
        dp[i][0] = i
    for j in range(len(t)+1):
        dp[0][j] = j

    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            c = 0 if s[i-1] == t[j-1] else 1
            temp1 = dp[i-1][j-1] + c
            temp2 = min(dp[i-1][j] + 1,dp[i][j-1]+1)
            dp[i][j] = min(temp1,temp2)
    return dp[len(s)][len(t)]

def main():
    s = input()
    t = input()
    print(henshu_kyori(s,t))

main()