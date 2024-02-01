

def topological_sort(graph):
    n = len(graph)
    in_cnt = [0 for _ in range(n)]
    used = [False for _ in range(n)]
    stack = []
    answer = []
    for i in range(n):
        for nxt in graph[i]:
            in_cnt[nxt] += 1
    for i in range(n):
        if in_cnt[i] == 0:
            stack.append(i)

    while stack:
        here = stack.pop()
        answer.append(here)
        for nxt in graph[here]:
            in_cnt[nxt] -= 1
            if in_cnt[nxt] == 0:stack.append(nxt)

    return answer



def main():
    n,m = map(int,input().split())
    graph = [list() for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)

    ans = topological_sort(graph)
    for line in ans:
        print(line)



if __name__ == '__main__':
    main()
