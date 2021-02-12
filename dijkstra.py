#ダイクストラ法

import heapq #優先度付きキュー


def dijkstra(graph,s=0,inf = 999999999999):
    # graph: グラフ本体。連結リスト。(次のノード,コスト)のタプルで表現
    # s: スタートノード
    num_of_nodes = len(graph)
    costs = [inf for _ in range(num_of_nodes)]
    before = [i for i in range(num_of_nodes)]
    fixed = [False for _ in range(num_of_nodes)] # 最小コストが確定したかのフラグ
    q = [] # 現在の最小コストを求めるためのヒープキュー
    num_of_not_fixed_node = num_of_nodes

    costs[s] = 0 # スタートノードのコストは0
    fixed[s] = True
    num_of_not_fixed_node -= 1
    heapq.heappush(q,(costs[s],s)) #コストが低いものを

    # 全てのノードの最小コストが確定するまでループ
    while num_of_not_fixed_node > 0:
        if not q:
            break
        _,shortest_node = heapq.heappop(q)
        fixed[shortest_node] = True
        for nxt,nxt_cost in graph[shortest_node]:
            if not fixed[nxt] and before[shortest_node] != nxt:
                if costs[nxt] > costs[shortest_node] + nxt_cost:
                    costs[nxt] = costs[shortest_node] + nxt_cost
                    before[nxt] = shortest_node
                heapq.heappush(q,(costs[nxt],nxt))
    return costs




def main():
    inf = 999999999999
    n,m,s = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
    costs = dijkstra(graph,s)
    for i in range(n):
        print(costs[i] if costs[i] != inf else "INF")

if __name__ == '__main__':
    main()
