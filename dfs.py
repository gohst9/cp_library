def dfs(lst:list,start:int,goal:int):
    #グラフの到達可能性（スタートからゴールへ至るルートがあるか）を判定するDFS
    #lst:隣接リスト。インデックスと同じ番号のノードから延びる別ノードへの行先が入っている
    #start:スタート
    #goal:ゴール
    check_lst = [start] #探索予定のノードを入れるリスト
    visited = [False for _ in lst] #調査済みのノードのインデックスの値はTrueになる(後戻り防止)

    while check_lst:
        check_i = check_lst.pop()
        if check_i == goal:
            return True
        if visited[check_i]:#調査済みのノードはスキップ
            continue
        visited[check_i] = True #現在調査中のインデックスを調査済みにする
        for next_i in lst[check_i]: #次に行くべきノードをcheck_lstに入れていく
            if visited[next_i]: #調査済みのノードはスキップ
                continue
            check_lst.append(next_i)

    return False


def main():
    n,k = map(int,input("n=ノードの数 k=辺の数").split())
    lst = [[] for _ in range(n)]
    for i in range(k):
        f,t = map(int,input().split())
        lst[f].append(t)
    s,g = map(int,input("s=スタート g=ゴール").split())
    print("possible" if dfs(lst,s,g) else "impossible")


if __name__ == '__main__':
    main()
