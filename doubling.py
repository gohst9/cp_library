def bin_power(a,n,mod=1000000007):
    ans = 1
    while n > 0:
        if n % 2 != 0:
            ans *= a
            ans %= mod
        a = a * a % mod
        n //= 2
    return ans

def doubling(lst,n):
    doubling_table = [[0 for _ in range(len(lst))] for _ in range(n)]
    doubling_table[0] = list(lst)
    for i in range(1,n):
        for j in range(len(lst)):
            doubling_table[i][j] = doubling_table[i-1][doubling_table[i-1][j]]

    return doubling_table

def main():
    lst = list(map(int,input().split()))
    n = int(input())
    print(doubling(lst,n))

main()




def main():
    a,n = map(int,input().split())
    print(bin_power(a,n))


