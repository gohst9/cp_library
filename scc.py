#参考記事　https://qiita.com/sysdev/items/4532d52ab9978cd9d4d4　　AtCoder Library を読んでアルゴリズムを勉強：強連結成分
#ACした問題 https://atcoder.jp/contests/practice2/submissions/50699894

import sys
sys.setrecursionlimit(999999) #再帰の深さを深めに設定

def scc(graph):
    n = len(graph)
    group_id = [-1 for _ in range(n)] #強連結成分のID。（降順に並ぶ）　
    new_order = 0 #今何番目に探索した頂点か
    order = [-1 for _ in range(n)]
    group_id_counter = 0
    visited_stack = [] #訪問した頂点のスタック
    def dfs(here):
        nonlocal n,new_order,group_id_counter
        if group_id[here] != -1: #すでに強連結成分のグループが確定している場合、無視
            return n
        if order[here] != -1: #探索順序がすでに割り振られている場合、それを返す
            return order[here]

        order[here] = new_order
        new_order += 1
        visited_stack.append(here)
        mn_ord = order[here]
        for nxt in graph[here]:
            mn_ord = min(mn_ord,dfs(nxt))

        if mn_ord < order[here]:
            return mn_ord

        while visited_stack:
            nxt = visited_stack.pop()
            group_id[nxt] = group_id_counter
            if nxt == here:
                break
        group_id_counter += 1
        return n #最大より上のグループIDを返すことで探索から外す

    for here in range(n):
        dfs(here)
    answer = [list() for _ in range(group_id_counter)]
    for here in range(n):
        answer[group_id[here]].append(here)

    for line in answer:
        line.sort(key=lambda x:order[x])
    answer = list(reversed(answer))
    return answer





def main():
    n,m = map(int,input().split())
    graph = [list() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
    ans = scc(graph)
    print(len(ans))
    for line in ans:
        print(len(line),*line)

if __name__ == '__main__':
    main()
