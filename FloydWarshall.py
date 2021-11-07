
def wf(graph,inf = 1 << 61):
    global total
    pre_graph = graph
    #graph[i][j] = iからjへ行くのにかかるコスト
    w = len(graph[0])
    h = len(graph)
    assert w == h,"グラフの形が不適切"
    for k in range(w):
        new_graph = [[inf for _ in range(w)] for _ in range(h)]
        for i in range(w):
            for j in range(w):
                new_graph[i][j] = min(pre_graph[i][j],pre_graph[i][k] + pre_graph[k][j])
                if new_graph[i][j] < inf:
                    total += new_graph[i][j]
        pre_graph = new_graph
    return new_graph

class Ad_lst:
    def __init__(self,n,directional = True,inf = 1 << 61):
        self.n = n
        self.lst = [[inf for _ in range(n)] for _ in range(n)]
        self.directional = directional
        self.graph_init()

    def add(self,a,b,cost,input_zero_indexed = False):
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
    pass


if __name__ == '__main__':
    main()
