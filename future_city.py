import sys
import heapq

INF = int(1e9)

input= sys.stdin.readline

n , m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n +1):
        for b in range(1, n +1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]
# 도달할 수 없는 경우
if distance >= INF:
    print(-1)
else:
    print(distance)