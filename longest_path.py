from functools import lru_cache

@lru_cache
def solve(x,graph):
    if len(graph[x]) == 0:
        return 0
    mx = -1
    for nxt in graph[x]:
        mx = max(mx,solve(nxt,graph))
    return mx + 1

def to_tuple(graph):
    #二次元リストを二次元タプルに
    return tuple([tuple(graph[x]) for x in range(len(graph))])

def main():
    n,m = map(int,input().split())
    graph = [list() for _ in range(n)]
    for _ in range(m):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
    mx = -1
    graph = to_tuple(graph)
    for i in range(n):
        mx = max(mx,solve(i,graph))
    
    print(mx)

main()