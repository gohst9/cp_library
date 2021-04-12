
#文字列の偶数文字目と奇数文字目を取り出す
def even_string(s):
    return s[1::2]
def odd_string(s):
    return s[::2]

#文字列が回文かどうかを判定
def is_kaibun(s):
    return s == s[::-1]


