
def wf(graph,inf = 1 << 61):
    total = 0 #ABC208 D問題　Shortest Path Queries 2用
    #graph[i][j] = iからjへ行くのにかかるコスト
    w = len(graph[0])
    h = len(graph)
    assert w == h,"グラフの形が不適切"
    for k in range(w):
        for i in range(w):
            for j in range(w):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
                if graph[i][j] < inf:
                    total += graph[i][j]
    return graph #,total

class Ad_lst:
    def __init__(self,n,directional = True,inf = float("inf")):
        self.n = n
        self.lst = [[inf for _ in range(n)] for _ in range(n)]
        self.directional = directional
        self.graph_init()

    def add(self,a,b,cost,input_zero_indexed = True):
        if not input_zero_indexed:
            a -= 1
            b -= 1
        self.lst[a][b] = cost
        if not self.directional:
            self.lst[b][a] = cost

    def get(self):
        return self.lst

    def graph_init(self):
        #隣接リストで、自分自身への移動コストを0にする
        n = len(self.lst)
        for i in range(n):
            self.lst[i][i] = 0




def main():
    n,m = map(int,input().split())
    graph = Ad_lst(n)
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph.add(a,b,c,input_zero_indexed = False)
    graph = graph.get()
    print(wf(graph))





if __name__ == '__main__':
    main()