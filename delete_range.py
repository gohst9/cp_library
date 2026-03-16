
#ABC435 E Cover query用

def delete_range(a,b,l,r):
    lst = []
    if l > b:
        lst.append([a,b])
        return lst
    if a < l and l <= b <= r:
        lst.append([a,l-1])
        return lst
    if a < l and r < b:
        lst.append([a,l-1])
        lst.append([r+1,b])
        return lst
    if l <= a <= r and r >= b:
        return lst
    if l <= a <= r and r < b:
        lst.append([r+1,b])
        return lst
    if r < a:
        lst.append([a,b])
        return lst

def main():
    a,b,l,r = map(int,input().split())
    print(delete_range(a,b,l,r))

    
main()

