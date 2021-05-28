from collections import deque

def main():
    n = 6
    graph =[[1],[2,3],[],[4],[5],[]]
    visited =[False] * n
    start = 0
    goal = 5
    pre_node = [False] * n
    dist = [0] * n
    q = deque()
    q.append(start)
    while q:
        here = q.popleft()
        visited[here] = True
        nxts = graph[here]
        nxts = [nxt for nxt in nxts if not visited[nxt]]
        for nxt in nxts:
            q.append(nxt)
            pre_node[nxt] = here
            dist[nxt] = dist[here] + 1

    print("距離=",dist[goal])
    #print(pre_node)
    here = goal
    route = [goal]
    while here != False:
        route.append(pre_node[here])
        here = pre_node[here]
    print(*reversed(route))


if __name__ == '__main__':
    main()
