inp = input().split()
n = int(inp[0])
m = int(inp[1])
factory = []
depths = []
cams = []
dirs = [[0,-1],[0,1],[1,0],[-1,0]]
convDirs = {'L':[0,-1],'R':[0,1],'D':[1,0],'U':[-1,0]}
convTypes = ['R','L','U','D']
init = [0,0]
for i in range(n):
    factory.append(input())
    depths.append([-1]*m)
    for k in range(len(factory[i])):
        j = factory[i][k]
        if j == 'S':
            init = [i,k]
            depths[i][k] = 0
        elif j == 'W':
            depths[i][k] = -2
        elif j == 'C':
            cams.append([i,k])
        else:
            depths[i][k] = -1
for i in cams:
    for j in dirs:
           pos = i
           border = 0
           if j[0] == 0:
               border = m
           else:
                border = n
           while 0<=pos[0]<=border:
               if factory[pos[0]][pos[1]] in convTypes:
                    pos = [pos[0]+j[0],pos[1]+j[1]]
                    continue
               elif factory[pos[0]][pos[1]] == 'W':
                    break
               depths[pos[0]][pos[1]] = -2
               pos = [pos[0]+j[0],pos[1]+j[1]]
queue = [init]
for i in queue:
    char = factory[i[0]][i[1]]
    depth = depths[i[0]][i[1]]
    if depth == -2:
        continue
    avDirs = dirs
    if char in convTypes:
        avDirs = [convDirs[char]]
    for j in avDirs:
        newPos = [i[0]+j[0],i[1]+j[1]]
        if depths[newPos[0]][newPos[1]] == -2:
            continue
        elif len(avDirs)==1:
            depths[newPos[0]][newPos[1]] = depth
        elif depths[newPos[0]][newPos[1]] > depth or depths[newPos[0]][newPos[1]] == -1:
            depths[newPos[0]][newPos[1]] = depth+1
        else:
            continue
        queue.append(newPos)
for i in range(n):
    for j in range(m):
        if factory[i][j]=='.':
            print(max(depths[i][j],-1))