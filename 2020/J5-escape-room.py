from math import sqrt
from math import floor
def main():
    m = int(input())
    n = int(input())
    grid = []
    mem = {}
    maxDig = max(m,n)
    for i in range(m):
        grid.append([int(i) for i in input().split()])
    q = [(0,0)]
    def poseMaker(val):
        if mem.get(val,None):
            return mem[val]
        poses = []
        for i in range(1,min(floor(sqrt(val)),maxDig)+1):
            otherCoord = val//i
            if otherCoord*i == val:
                #in theory, can be accessible, divides roundly
                poses.append((i-1,otherCoord-1))
                poses.append((otherCoord-1,i-1))
                if (m-1,n-1) in poses[len(poses)-2:]:
                    print("yes")
                    exit()
        mem[val] = poses
        return poses
    visited = {}
    while q:
        current = q.pop(0)
        if visited.get(current,None):
            continue
        visited[current] = True
        poses = []
        val = grid[current[0]][current[1]]
        poses = poseMaker(val)
        for i in poses:
            if i[0]<m and i[1]<n:
                q.append(i)
    print("no")
main()