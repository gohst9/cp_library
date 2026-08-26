from collections import deque
import unittest


def bfs(graph,s=0):
    here = 0
    n = len(graph)
    deq = deque()
    depth = [-1 for _ in range(n)]

    deq.append((0,here))
    while deq:
        d,here = deq.popleft()
        if depth[here] != -1:
            continue
        depth[here] = d

        for nxt in graph[here]:
            if depth[nxt] != -1:
                continue
            deq.append((d+1,nxt))



    return depth 


def doubling(graph,s=0,power = 20):
    n = len(graph)
    temp = [i for i in range(n)]
    parents = [[s for _ in range(n)]]
    for i in range(n):
        for child in graph[i]:
            temp[child] = i
    parents[0] = temp

    for i in range(0,power):
        temp = [-1 for _ in range(n)]
        for j in range(n):
            temp[j] = parents[-1][parents[-1][j]]
        parents.append(temp)

    return parents


def lca(a,b,depth,parents,power = 20):
    #depth = bfs(graph)
    #parents = doubling(graph,power=power)
    if depth[a] > depth[b]:
        a,b = b,a

    for i in range(power,-1,-1):

        if depth[b] - depth[a] >= 2**i :
            b = parents[i][b]

    if a > b:
        a,b = b,a
    while depth[b] > depth[a]:
        b = parents[0][b]

    while a != b:
        a = parents[0][a]
        b = parents[0][b]


    return a





def main():
    n = int(input())
    graph = []
    for _ in range(n):
        temp  = list(map(int,input().split()))
        graph.append(temp[1:])
    depth = bfs(graph)
    parents = doubling(graph)
    q = int(input())

    ans = []
    for i in range(q):
        u,v = map(int,input().split())
        temp = lca(u,v,depth,parents)
        ans.append(temp)

    for line in ans:
        print(line)
        



class test(unittest.TestCase):


    def test_bfs1(self):
        graph = [[1],[2],[]]
        depth = bfs(graph)
        exp = [0,1,2]
        self.assertEqual(depth,exp)


    def test_bfs2(self):
        graph = [[1,2],[3],[],[]]
        depth = bfs(graph)
        exp = [0,1,1,2]
        self.assertEqual(depth,exp)



#unittest.main()

main()