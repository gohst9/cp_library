def main():
    n = int(input())
    print(prime_fact(n))

def prime_fact(n):
    temp = n
    if n == 1:
        return []
    facts = []
    while temp % 2 == 0:
        temp //= 2
        facts.append(2)

    for i in range(3,n//2+1,2):
        while temp % i == 0:
            facts.append(i)
            temp //= i
    return facts


if __name__ == '__main__':
    main()
