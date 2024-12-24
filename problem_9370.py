import heapq
import sys
input = sys.stdin.readline
INF =int(1e9)
def dijkstra(start):
    distance[start][0] =0
    q =[]
    heapq.heappush(q,(0,start,False))
    while q:
        dist, now, bool = heapq.heappop(q)
        if distance[now][0] < dist:
            continue
        for i in array[now]:
            cost = dist + i[1]
            if distance[i[0]][0] >= cost:
                distance[i[0]][0] = cost
                if i[2] or bool:
                    distance[i[0]][1] = True
                    bool = True
                heapq.heappush(q,(cost,i[0],bool))



T = int(input())
result = [[] for _ in range(T)]

for c in range(T):
    n,m,t = map(int,input().split())    
    s,g,h = map(int,input().split())
    array = [[] for _ in range(n+1)]
    distance =[[INF,False] for _ in range(n+1)]
    end= []
    for _ in range(m):
        a,b,d = map(int,input().split())
        if (a==g and b == h) or (a==h and b==g):
            array[a].append([b,d,True])
            array[b].append([a,d,True])
        else:
            array[a].append([b,d,False])
            array[b].append([a,d,False])
    for _ in range(t):
        heapq.heappush(end,int(input()))
    dijkstra(s)
    for i in end:
        if distance[i][1]:
            result[c].append(i)
        
for i in result:
    for a in i:
        print(a, end=' ')
    print()
