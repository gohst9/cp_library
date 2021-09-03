
def furui(n):
    lst = [False] + [i for i in range(1,n+1)]
    for i in range(4,n+1,2):
        lst[i] = False

    for i in range(3,int(n ** 0.5)+1,2):
        if not lst[i]:
            continue
        for j in range(i+i,n+1,i):
            lst[j] = False

    lst = list(set(lst))
    lst.sort()
    return lst[2:]





def main():
    n = int(input())
    print(furui(n))

if __name__ == '__main__':
    main()
