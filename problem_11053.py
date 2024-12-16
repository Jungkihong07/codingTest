# [백준]11053번 가장 긴 증가하는 부분 수열
n = int(input())
graph = list(map(int,input().split()))
dp = [1] * n
for i in range(1,n):
    for j in range(0,i):
        if graph[j]<graph[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))