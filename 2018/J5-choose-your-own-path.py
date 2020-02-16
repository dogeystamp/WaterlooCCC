#Written by DogeyStamp as practice.
#15/15 points
#Breadth-First-Search.
#We build an adjacency list, then do the algorithm on it.
#mindepth is minimum depth to get to end page.
#At the end, if there still is a 100001 (unvisited) page, print N.
#Also print mindepth.
nopages = int(input())
depths = []
adj = []
mindepth = 10001
for i in range(nopages):
    adj.append([])
    page = input().split()
    page.pop(0)
    for j in page:
        adj[i].append(int(j))
    depths.append(10001)
depths[0] = 0
q = [1]
while q:
    p = q.pop(0)
    if len(adj[p-1]) == 0:
        mindepth = min(mindepth,depths[p-1])
    for i in adj[p-1]:
        if depths[i-1]==10001:
            q.append(i)
            depths[i-1]=depths[p-1]+1
if not 10001 in depths:
    print("Y")
else:
    print("N")
print(mindepth+1)