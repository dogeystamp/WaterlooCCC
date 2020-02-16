p = int(input())
n = int(input())
r = int(input())
inf = n
newInf = n
day = 0
while inf <= p:
    newInf = r*newInf
    inf += newInf
    day += 1
print(day)