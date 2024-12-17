# [백준] 13549번 숨바꼭질3
import heapq

INF = int(1e9)

MAX = 1000000

graph = [INF]* (MAX +1)

n, k = map(int,input().split())

def solve(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cnt, now = heapq.heappop(q)
        if now == k:
            return cnt
        for i in (now-1, now +1, now*2):
            if 0<= i <= MAX:
                if graph[i] > cnt:
                    graph[i] = cnt
                    if i == now*2:
                        heapq.heappush(q,(cnt, i))
                    else:
                        heapq.heappush(q,(cnt+1, i))
print(solve(n))