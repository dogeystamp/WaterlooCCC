n = int(input())
m = []
for j in range(n):
    m.append([int(i) for i in input().split()])
m.sort()
rec = 0
for i in range(n-1):
    rec = max(rec,abs(m[i-1][1]-m[i][1])/(m[i][0]-m[i-1][0]))
print(rec)