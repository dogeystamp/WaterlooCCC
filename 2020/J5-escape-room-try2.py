#Written by DogeyStamp during the 2020 CCC.
#13/15 points
#Time limit exceeded on last subtask, granting 0/2 points
#A backwards Breadth-First-Search (BFS) solution.
#Takes the coordinates of a point to find where other points that could lead to it are.
#We multiply x and y in the coordinates, then see what points have the value.
def main():
    m = int(input())
    n = int(input())
    #Find the size of the grid
    endVal = 0
    gridValSearch = {}
    for i in range(m):
        line = [int(i) for i in input().split()]
        if i == 0:
            endVal = line[0]
            #This is the value of the point at 0,0
        for j in range(n):
            val = line[j]
            if not gridValSearch.get(val,False):
                gridValSearch[val] = [(i,j)]
            else:
                gridValSearch[val].append((i,j))
    #Essentially, we have a dictionary (gridValSearch) where Value goes in, coordinates with the Value goes out.
    q = [(m-1,n-1)]
    #BFS queue
    visited = {}
    #BFS visited
    while q:
        #Standard BFS
        pos = q.pop()
        if visited.get(pos,False):
            #Make sure this isn't visited
            continue
        visited[pos] = True
        if (pos[0]+1)*(1+pos[1]) == endVal:
            #If this place can go to the start (end because this is backwards), say yes
            print("yes")
            exit()
        newStuff = gridValSearch.get((pos[0]+1)*(1+pos[1]),[])
        q = q + newStuff
        #Since you can go to any coordinate where x*y is the value of your current point,
        #we do x*y of current point and find coordinates with that value in the dict.
        #We then add that to the queue.
    print("no")
    #If we exhaust all choices, abandon
main()
#Main function for speed, I guess it didn't work