# 벨만 포드 알고리즘 (시간 복잡도 2753ms)
import sys

INF = sys.maxsize
n = int(input())
m = int(input())


edges = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))
start, end = map(int, input().split())
dist = [sys.maxsize] * (n + 1)


# 벨만 포드 알고리즘 수행
def bf(start):
    dist[start] = 0
    for i in range(n):
        updated = False
        for j in range(m):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                updated = True
        if not updated:
            break
    return False


bf(start)
print(dist[end])
