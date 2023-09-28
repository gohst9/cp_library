import math

def factorize(n):
    factor_counter = []
    temp = n
    for i in range(2,math.ceil(math.sqrt(n))):
        if temp%i !=0:
            continue
        fact_count = 0
        while temp % i == 0:
            fact_count += 1
            temp //= i
        factor_counter.append((i,fact_count))

    #最後に素数が残っているとき
    if temp != 1:
        factor_counter.append((temp,1))

    #nが素数のとき
    if not factor_counter:
        factor_counter.append((n,1))

    return factor_counter




def main():
    n = int(input())
    print(factorize(n))

if __name__ == '__main__':
    main()
