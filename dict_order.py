from functools import lru_cache


@lru_cache(9999999)
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

def dict_order(lst,n):
    lst = list(sorted(lst))
    used = set()

    ans = []
    for i in range(len(lst)):
        temp = fact(len(lst)-1)
        ans.append(lst[n//temp])
        del lst[n//temp]
        n %= temp
    return ans


def main():
    n = int(input())
    lst = list(map(int,input().split()))
    print(dict_order(lst,n))


main()