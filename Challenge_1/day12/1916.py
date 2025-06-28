# 다익스트라 알고리즘 정석. 324ms 걸림.(역시 최적화가 최고)
import heapq
import sys

input = sys.stdin.readline

n = int(input())  # 도시의 갯수 입력
m = int(input())  # 버스의 갯수 입력

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

# start를 기준으로 거리 계산
dist = [sys.maxsize] * (n + 1)

dist[start] = 0

heap = []

# cost와 출발지 입력
heapq.heappush(heap, (0, start))

while heap:
    cost, now = heapq.heappop(heap)

    if dist[now] < cost:
        continue

    for next_node, weight in graph[now]:
        new_cost = cost + weight
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))
print(dist[end])
