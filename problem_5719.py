import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dist =[INF] * (n)

    dist[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in array[now]:
            if edges[now][i[0]]: continue
            cost =  distance + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return dist

def bfs():
    q = deque()
    q.append(d)
    
    while q:
        current = q.popleft()

        if current == s:
            continue
        for node, cost in array_inv[current]:
            if dist[node] + cost == dist[current] and not edges[node][current]:
                edges[node][current] = True
                q.append(node)

result = []
while 1:
    n,m = map(int,input().split())

    if not (n and m):
        break
    s,d = map(int,input().split())

    array =[[] for _ in range(n)]
    array_inv =[[] for _ in range(n)]
    edges = [ [False]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        array[u].append([v,p])
        array_inv[v].append([u,p])

    dist = dijkstra(s)
    bfs()
    dist = dijkstra(s)
    result.append(-1 if dist[d] == INF else dist[d])

for a in result:
    print(a)