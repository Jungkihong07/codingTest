# [백준] 1753번 최단 경로
import heapq
import sys

input = sys.stdin.readline
v,e = map(int,input().split())

start = int(input())

INF =int(1e9)

graph = [[] for _ in range(v+1)]

distance = [INF] * (v+1)

for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


def dijkstra(start):
    q =[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
dijkstra(start)

for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)