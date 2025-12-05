from collections import deque
import unittest

class Flow:
    def __init__(self,edges,n):
        self.INF = 10 ** 30
        self.n = n
        self.graph = [list() for _ in range(n)]
        for u,v,c in edges:
            self.add_edge(u,v,c)
        


    def add_edge(self,u,v,c):
        rev = len(self.graph[v])
        self.graph[u].append([v,c,rev])
        self.graph[v].append([u,0,len(self.graph[u])-1])


    def level_bfs(self,s,t):
        levels = [-1 for _ in range(self.n)]
        levels[s] = 0
        d = deque()
        d.append(s)
        while d:
            here = d.popleft()
            for nxt,cap,rev in self.graph[here]:
                if cap <= 0 or levels[nxt] != -1:
                    continue
                levels[nxt] = levels[here] + 1
                d.append(nxt)
    
        return levels

    def dfs(self,here,goal,f,seen,levels):
        if here == goal:
            return f

        while seen[here] < len(self.graph[here]):
            nxt,cap,rev = self.graph[here][seen[here]]
            if cap > 0 and levels[here] < levels[nxt]:
                flow = self.dfs(nxt,goal,min(f,cap),seen,levels)
                if flow > 0:
                    self.graph[here][seen[here]][1] -= flow
                    self.graph[nxt][rev][1] += flow
                    return flow
            seen[here] += 1
        return 0


    def calc(self,start,goal):
        flow = 0

        while True:
            levels = self.level_bfs(start,goal)
            if levels[goal] < 0:
                return flow
            seen = [0 for _ in range(self.n)]
            while True:
                f = self.dfs(start,goal,self.INF,seen,levels)
                if f == 0:
                    break
                flow += f




class Test(unittest.TestCase):

    def test_1(self):
        n = 4
        v = 4
        edges = [[0,1,2],[0,2,1],[1,2,1],[2,3,2]]
    
        ans = Flow(edges,n,0,v-1)
        self.assertEqual(ans,2)

    
#unittest.main()

def main():
    V,E = map(int,input().split())
    graph = [list() for _ in range(V)]
    edges = []
    for _ in range(E):
        u,v,c = map(int,input().split())
        edges.append([u,v,c])
    flow = Flow(edges,V)
    ans = flow.calc(0,V-1)
    print(ans)


main()