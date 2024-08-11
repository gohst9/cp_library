class Csum_3d:
    def __init__(self,cuboid):
        w = len(cuboid)
        h = len(cuboid[0])
        d = len(cuboid[0][0])

        csum = [[[0 for _ in range(d+1)] for _ in  range(h+1)] for _ in range(w+1)]
        for x in range(w):
            for y in range(h):
                for z in range(d):
                    csum[x+1][y+1][z+1] = csum[x][y+1][z+1] + csum[x+1][y][z+1] + csum[x+1][y+1][z] -\
                    csum[x+1][y][z] - csum[x][y+1][z] - csum[x][y][z+1] + csum[x][y][z] + cuboid[x][y][z]

        self.csum = csum

    def query(self,x1,y1,z1,x2,y2,z2):
        #0-indexed 半開区間
        csum = self.csum
        return csum[x2][y2][z2] - csum[x1][y2][z2] - csum[x2][y1][z2] - csum[x2][y2][z1] +\
               csum[x1][y1][z2] + csum[x1][y2][z1] + csum[x2][y1][z1] - csum[x1][y1][z1]

