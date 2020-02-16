def main():
    m = int(input())
    n = int(input())
    endVal = 0
    gridValSearch = {}
    for i in range(m):
        line = [int(i) for i in input().split()]
        if i == 0:
            endVal = line[0]
        for j in range(n):
            val = line[j]
            if not gridValSearch.get(val,False):
                gridValSearch[val] = [(i,j)]
            else:
                gridValSearch[val].append((i,j))
    q = [(m-1,n-1)]
    visited = {}
    while q:
        pos = q.pop()
        if visited.get(pos,False):
            continue
        visited[pos] = True
        if (pos[0]+1)*(1+pos[1]) == endVal:
            print("yes")
            exit()
        newStuff = gridValSearch.get((pos[0]+1)*(1+pos[1]),[])
        q = q + newStuff
    print("no")
main()