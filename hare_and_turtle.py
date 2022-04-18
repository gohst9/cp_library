def hare_and_turtle(lst):
    har = 0
    tur = 0

    while True:
        har = lst[lst[har]]
        tur = lst[tur]
        if har == tur:
            break

    har = 0
    while har != tur:
        har = lst[har]
        tur = lst[tur]
    l = 1
    har = lst[har]
    while har != tur:
        har = lst[har]
        l += 1

    return har,l




def main():
    lst = list(map(int,input().split()))
    print(hare_and_turtle(lst))

if __name__ == '__main__':
    main()
