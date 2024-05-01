def bin_power(a,n,mod=1000000007):
    ans = 1
    while n > 0:
        if n % 2 != 0:
            ans *= a
            ans %= mod
        a = (a * a) % mod
        n //= 2
    return ans % mod

def nCr(n,r,mod=1000000007,kaijo=None,gyakugen=None):
    x = 1
    y = 1
    #事前に階乗テーブル、階乗の逆元テーブルを使わない場合
    if kaijo==None and gyakugen==None:
        for i in range(r):
            x *= (n-i)
            x %= mod
            y *= (i+1)
            y %= mod
        return (x * bin_power(y,mod-2,mod)) % mod

    #事前に階乗テーブル、階乗の逆元テーブルを事前計算した場合
    else:
        x = (kaijo[n] * gyakugen[n-r]) % mod
        y = gyakugen[r] % mod
        return (x * y)%mod


def create_kaijo_table(n,mod=10**9+7):
    kaijo = [0 for _ in range(n+1)]
    kaijo[0] = 1
    for i in range(1,n+1):
        kaijo[i] = kaijo[i-1]*i % mod
    kaijo[0] = 1
    return kaijo
def create_gyakugen_table(n,kaijo,mod=10**9+7):
    gyakugen = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        gyakugen[i] = bin_power(kaijo[i],mod-2,mod) % mod
    gyakugen[0] = 1
    return gyakugen


def main():
    #ABC021 D問題で確認
    n = int(input())
    k = int(input())
    mod = 10**9+7
    kaijo = create_kaijo_table(n+k,mod)
    gyakugen = create_gyakugen_table(n+k,kaijo,mod)
    print(nCr(n+k-1,k,mod,kaijo,gyakugen))

if __name__ == '__main__':
    main()
