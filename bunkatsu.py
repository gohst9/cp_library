def dfs(lst,idx,sz,group,ans):
    for i in range(sz+1):
        
        group[i].append(lst[idx])
        if idx == len(lst)-1:
            ans.append([list(g) for g in group])
        elif i < sz:
            dfs(lst,idx+1,sz,group,ans)
        else:
            dfs(lst,idx+1,sz+1,group,ans)
        group[i].pop()

def main():
    lst = list(map(int,input().split()))
    group = [list() for _ in range(len(lst))]
    ans = []
    dfs(lst,0,0,group,ans)
    for line in ans:
        print(line)

main()








