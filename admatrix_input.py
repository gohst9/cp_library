#ABC450みたいな隣接行列の入力形式に対応する関数



def make_admatrix(n,lst):
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            graph[i][j] = lst[i][j-i-1]
    return graph

n = int(input())
lst = []
for i in range(n-1):
    lst.append(list(map(int,input().split())))


ans = make_admatrix(n,lst)
for line in ans:
    print(line)

