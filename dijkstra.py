def dijkstra(graph,s=0,inf = 999999999999):
    #graphは隣接行列
    #sはスタート地点
    n = len(graph) #グラフの長さ
    costs = [inf for _ in range(n)] #移動にかかるコスト
    fixed = [False for _ in range(n)] #確定フラグ
    costs[s] = 0 #スタート地点はコストゼロ
    while True:
        mn_index = -1
        mn = inf
        #現在もっとも移動コスト小さいがノードを見つける
        for i,cost in enumerate(costs):
            if fixed[i]:
                continue
            if cost < mn:
                mn = cost
                mn_index = i
        #未確定ノードが無かった場合ループから抜ける
        if mn_index == -1:
            break
        fixed[mn_index] = True
        for nxt,cost in enumerate(graph[mn_index]):
            costs[nxt] = min(costs[nxt],costs[mn_index] + cost)
    return costs



def main():
    inf = 999999999999
    n,m = map(int,input().split()) #n個のノードにm個の辺
    s,g = map(int,input().split())
    graph = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0 #自分自身への移動はコスト0
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a][b] = c
    costs = dijkstra(graph,s,inf)
    print(costs[g])



if __name__ == '__main__':
    main()
