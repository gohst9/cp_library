

def points_to_line(a1,b1,a2,b2):
    #直線の一般系　ax + by + c = 0
    return [(b2-b1),(a1-a2),a2*b1-a1*b2]

def cross_point(line1,line2):
    a1,b1,c1 = line1
    a2,b2,c2 = line2
    if a1 * b2 -a2 * b1 == 0:
        return False
    return ((b1*c2-b2*c1)/(a1*b2-a2*b1),(a2*c1 - a1*c2)/(a1*b2 - a2*b1))


def main():
    a1,b1,a2,b2 = map(int,input().split())
    line1 = points_to_line(a1,b1,a2,b2)
    a1,b1,a2,b2 = map(int,input().split())
    line2 = points_to_line(a1,b1,a2,b2)
    print(line1)
    print(line2)
    print(cross_point(line1,line2))

main() 