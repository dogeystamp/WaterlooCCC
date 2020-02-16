#Written by DogeyStamp during the 2020 CCC.
#13/15 points
#Time limit exceeded on last subtask, granting 0/2 points
#A regular BFS solution
from math import sqrt
from math import floor
def main():
    m = int(input())
    n = int(input())
    #Get grid size
    grid = []
    mem = {}
    maxDig = max(m,n)
    for i in range(m):
        grid.append([int(i) for i in input().split()])
    #Read the grid values
    q = [(0,0)]
    #Queue for BFS
    def poseMaker(val):\
        #Generate some positions
        if mem.get(val,None):
            #Check if the outcome of this function hasen't already been computed
            #We don't waste time here
            return mem[val]
        poses = []
        for i in range(1,min(floor(sqrt(val)),maxDig)+1):
            #Messy for loop, essentially finds divisors of the value
            otherCoord = val//i
            if otherCoord*i == val:
                #in theory, can be accessible, divides roundly
                poses.append((i-1,otherCoord-1))
                poses.append((otherCoord-1,i-1))
                if (m-1,n-1) in poses[len(poses)-2:]:
                    #If the end position is in sight, say yes immediately
                    print("yes")
                    exit()
        mem[val] = poses
        return poses
    visited = {}
    #Visited list for BFS
    while q:
        #Standard BFS implementation
        current = q.pop(0)
        if visited.get(current,None):
            continue
        # If visited, continue
        visited[current] = True
        poses = []
        val = grid[current[0]][current[1]]
        #Value at current grid position
        poses = poseMaker(val)
        #Generate possible places we can go to
        for i in poses:
            if i[0]<m and i[1]<n:
                #For every position, verify it doesn't go out the grid, then add to queue
                q.append(i)
    #When we exhaust all possibilities, say no
    print("no")
main()