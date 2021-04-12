
#文字列の偶数文字目と奇数文字目を取り出す
def even_string(s):
    return s[1::2]
def odd_string(s):
    return s[::2]

#文字列が回文かどうかを判定
def is_kaibun(s):
    return s == s[::-1]

#2進数に変換して1と0の文字列で返す
def return_binary_string(n):
    return bin(n)[2:]


#完全2分木が作れるようにリストの要素を埋める
def CBT_fill(lst,monoid=0):
    size = len(lst)
    n = 1
    while n < size:
        n *= 2
    return lst + [monoid] * (-size%n)



