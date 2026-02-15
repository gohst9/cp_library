
def bin_power(a,n,mod=1000000007):
    ans = 1
    while n > 0:
        if n & 1:
            ans *= a
            ans %= mod
        a = a * a % mod
        n >>= 1
    return ans

def mod_div(a,b,mod):
    #modでのa / bを返す
    #modは素数
    inv = mod-2 #フェルマーの小定理の逆元の指数
    return a * bin_power(b,inv,mod) % mod


print("tst")