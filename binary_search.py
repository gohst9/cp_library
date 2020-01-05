
def binary_search(l:list,a:int):
    #リストlからaの値のインデックスをサーチする。
    #二分探索を可能にするためにはリストlはソートされていなければならない。
    length = len(l)
    center = length//2
    low = 0
    high = length - 1
    while low <= high:
        if l[center] == a:
            return center
        elif l[center] < a:
            low = center + 1
        elif l[center] > a:
            high = center - 1

        center = (low + high) // 2
    print("リスト内に指定した数値が存在しません。")
    return None

def main():
    lst1 = [3,4,8,12]  #ソートされたリスト
    lst2 = [5,3,2,9]   #ソートされていないリスト
    lst3 = [2,2,2,2,2] #要素が重複しているリスト　
    print(binary_search(lst1,8)) #ソートされたリスト内からは対象の数値を発見できる。
    print(binary_search(lst2,5)) #ソートされていないリストだと対象を発見できないことがある。
    print(binary_search(lst3,2)) #要素が重複している場合、重複しているうちのどのインデックスが返るかは保証されていない。
                                 #二分割していきながら探索するので真ん中,4分割点、8分割点……の近くが優先して探索される。

if __name__ == '__main__':
    main()
