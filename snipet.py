
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

#ふたつのリストの要素が一致するところは1、一致しないところは0のリストを返す
def list_or(lst1,lst2):
    if len(lst1) != len(lst2):
        return None
    length = len(lst1)
    new_lst = [0] * length
    for i in range(length):
        if lst1[i] == lst2[i]:
            new_lst[i] = lst1[i]

    return new_lst

#9の倍数かどうかを判定（すべての桁の総和を求めることを1桁になるまで繰り返す）
def is_multiple_of_nine(n):
    s = str(n)
    while len(s) > 1:
        digit_total = 0
        for c in s:
            digit_total += int(c)

        s = str(digit_total)
    return int(s) == 9

#test
#test2
#test3
#test4
#test5