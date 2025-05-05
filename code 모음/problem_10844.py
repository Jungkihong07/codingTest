# 10844번 쉬운 계단 수
n = int(input())

array = [[0]*(10) for _ in range(n + 1)]


for i in range(1,10):
    array[1][i] = 1
        
for i in range(2,n+1):
    for j in range(10):
        if j>0:
            array[i][j] += array[i-1][j-1]
        if j<9:
            array[i][j] += array[i-1][j+1]
        array[i][j] %= 1000000000

print(sum(array[n])%1000000000)
