#深さ優先探索　引数を変数contextに入れて渡して見る

def dfs(here=0,temp=[],goal=0,answer=[],graph=[],seen=[],**others):

    if here == goal:
        answer.append(tuple(temp))
        return

    for nxt in graph[here]:
        if seen[nxt]:
            continue
        temp.append(nxt)
        seen[nxt] = True
        nxt_context = locals()
        nxt_context["here"] = nxt
        dfs(**nxt_context)
        temp.pop()
        seen[nxt] = False






def main():
    n = int(input("ノードの数："))
    graph = [[] for _ in range(n)]
    m = int(input("辺の数:"))
    for i in range(m):
        a,b = map(int,input("a,b:").split())
        graph[a].append(b)

    start = int(input("スタート:"))
    goal = int(input("ゴール:"))
    seen = [False] * n
    answer = []
    context = {"here":start,"seen":seen,"graph":graph,"goal":goal,"answer":answer,"temp":[]}
    context["temp"].append(start)
    context["seen"][start] == True
    dfs(**context)
    print(answer)

if __name__ == '__main__':
    main()
