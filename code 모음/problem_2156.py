n = int(input())
graphes =[]

for _ in range(n):
    graphes.append(int(input()))

array = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        array[i][j] 