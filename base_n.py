def base_n_to_decimel(x,n):
    ans = 0
    if type(x) == int:
        x = str(x)
    assert type(x) == str
    for i in range(len(x)):
        if x[-(i+1)].isalpha():
            c = x[-(i+1)]
            c = c.upper()
            d = ord(c) - 65 + 10
        else:
            d = int(x[-(i+1)])
        d *= (n**i)
        ans += d

    return ans

def decimel_to_base_n(x,n):
    ans = []
    if x == 0:
        return "0"
    while x > 0:
        d = x % n
        x //= n
        if d >= 10:
            d = str(chr(d-10+65))

        d = str(d)
        ans.append(d)
    return "".join(reversed(ans))