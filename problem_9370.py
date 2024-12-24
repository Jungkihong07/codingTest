import heapq
import sys
input = sys.stdin.readline
INF =int(1e9)
def dijkstra(start):
    distance[start] =0
    q =[]
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in array[now]:
            cost = dist + i[1]
            if distance[i[0]][0] > cost:
                distance[i[0]][0] = cost
                if i[2]:
                    distance[i[0]][1] = True
                heapq.heappush(q,(cost,i[0]))



T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())    
    s,g,h = map(int,input().split())
    array = [[] for _ in range(n+1)]
    distance =[[INF,False] for _ in range(n+1)]
    end= []
    for _ in range(m):
        a,b,d = map(int,input().split())
        if a==(g or h) and b == (g or h):
            array[a].append([b,d,True])
            array[b].append([a,d,True])
        else:
            array[a].append([b,d,False])
            array[b].append([a,d,False])
    for _ in range(t):
        heapq.heappush(end,int(input()))
    dijkstra(s)
    result = []
    for i in end:
        if distance[i][1]:
            print(i)
        