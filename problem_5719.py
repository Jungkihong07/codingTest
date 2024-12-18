import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)



n,m = map(int,input().split())

s,d = map(int,input().split())

dist =[INF] * (n)

array =[[] for _ in range(n)]

for _ in range(m):
    u,v,p = map(int,input().split())
    array[u].append([v,p])

def dijkstra(start):
    dist[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in array[now]:
            cost =  distance + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))