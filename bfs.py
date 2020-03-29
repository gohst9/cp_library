from collections import deque

def bfs(graph,v=0):
    #args:
    #   graph グラフ本体
    #   v 現在注目しているノード（スタート地点）
    dist = [-1]*len(graph)
    q = deque()
    q.append(v)
    dist[v] = 0
    while q:
        d = dist[v]
        v = q.popleft()
        for v in graph[v]:
            if dist[v] != -1:
                continue
            else:
                q.append(v)
                dist[v] = d+1
    return dist


def main():
    print(bfs([[4],[],[],[],[]],0))
    print(bfs([[1,2,3],[],[],[4],[0]]))

if __name__ == '__main__':
    main()
