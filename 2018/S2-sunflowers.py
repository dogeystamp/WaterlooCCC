rows = []
size = int(input())
for i in range(size):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    rows.append(row)
def rotate():
    bufferows = []
    for i in range(size):
        bufferows.append([])
        for j in range(size):
            bufferows[i].append(rows[i][j])
    for i in range(size):
        for j in range(size):
            item = bufferows[i][j]
            rows[size-j-1][i] = item
while rows[0][0] > rows[0][1] or rows[0][0]>rows[1][0]:
    rotate()
for i in range(size):
        for j in range(size):
            print(rows[i][j],end = " ")
        print("")