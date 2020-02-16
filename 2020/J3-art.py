n = int(input())
minX,minY = 100,100
maxX,maxY = 0,0
for i in range(n):
    x,y = [int(i) for i in input().split(",")]
    minX, minY = min(minX,x), min(minY,y)
    maxX, maxY = max(maxX,x), max(maxY,y)
print(str(minX-1) + "," + str(minY-1))
print(str(maxX+1) + "," + str(maxY+1))