#Written by DogeyStamp during the 2020 CCC.
#15/15 points
#Get the 2 coordinates that are the furthest in the bottom-left and top-right direction, respectively.
#Make your frame go just a bit over these points, and that's your frame size.
#Example: Your points are 2,2 and 3,3
#Your frame goes 1,1 and 4,4
#Example 2: Your points are 2,5 and 3,3
#Your coords are 2,3 and 3,5
#Your frame is 1,2 and 4,6
n = int(input())
minX,minY = 100,100
maxX,maxY = 0,0
for i in range(n):
    x,y = [int(i) for i in input().split(",")]
    minX, minY = min(minX,x), min(minY,y)
    maxX, maxY = max(maxX,x), max(maxY,y)
print(str(minX-1) + "," + str(minY-1))
print(str(maxX+1) + "," + str(maxY+1))