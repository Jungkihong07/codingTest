# 백준 9370 미확인 도착지
import heapq
import sys
input = sys.stdin.readline
INF =int(1e9)

def dijkstra(start, distance):
    distance[start] =0
    q =[]
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in array[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost                
                heapq.heappush(q,(cost,i[0]))



T = int(input())
result = [[] for _ in range(T)]
for c in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    array = [[] for _ in range(n+1)]
    distance =[INF for _ in range(n+1)]
    dist_g = [INF for _ in range(n+1)]
    dist_h = [INF for _ in range(n+1)]
    ends= []
    for _ in range(m):
        a,b,d = map(int,input().split())
        array[a].append([b,d])
        array[b].append([a,d])
    for _ in range(t):
        heapq.heappush(ends,int(input()))
    dijkstra(s, distance)
    dijkstra(g, dist_g)
    dijkstra(h, dist_h)
    for end in ends:
        if (distance[end] == distance[g] + dist_g[h] + dist_h[end]) or (distance[end] == distance[h] + dist_h[g] + dist_g[end]):
            heapq.heappush(result[c], end)
        
for i in result:
    i.sort()
    print(*i)
