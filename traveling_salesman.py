
#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c
#典型アルゴリズム問題集　C - 巡回セールスマン問題で確認

def solve(n,a,INF = 10 ** 10000):
    #n:都市数
    #a:都市間の道路のコストを表す隣接行列
    #INF:適当にデカイ数


    dp = [[INF for _ in range(n)] for _ in range(1<<n)]
    #dp[b][v] 行ったことのある都市の集合を表す2進数b、その集合の中で最後に行った都市v
    dp[1][0] = 0 #スタート地点はコスト0　（別にどこを初期地点にしても変わらない）

    for b in range(1 << n):
        for u in range(n):
            for v in range(n):
                if u == v:
                    continue
                #すでに行った都市の中にuがあって、vにまだ行ったことがないなら、
                #最後にuに訪れたパターンからvへの移動コストを比較する
                if (1 << u & b) and not (1 << v & b):
                    dp[b|(1<<v)][v] = min(dp[b|(1<<v)][v],dp[b][u] + a[u][v])
    
    ans = min([dp[-1][v] + a[v][0] for v in range(n)])
    return ans


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int,input().split())))
    
    print(solve(n,a))

main()