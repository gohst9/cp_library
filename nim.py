def nim(lst):
    xor_sum = 0
    for a in lst:
        xor_sum ^= a
    return xor_sum

def main():
    lst = map(int,input().split())
    print(nim(lst))

if __name__ == '__main__':
    main()
