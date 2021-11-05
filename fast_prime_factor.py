def fast_prime_factor(n):
    D = [i for i in range(n+1)]
    for i in range(2,int(n ** 0.5)+1):
        for j in range(i,n+1,i):
            if D[j] != j:
                continue
            D[j] = i

    return D #「その数を最初に振るい落とした素数」のリストを返す（0,1に対しては使わない前提）
    #return [D[i] for i in range(len(D)) if D[i] == i][2:]
    #↑nまでの素数リストを返したいときはこっち

def main():
    n = int(input())
    print(*fast_prime_factor(n))

if __name__ == "__main__":
    main()
