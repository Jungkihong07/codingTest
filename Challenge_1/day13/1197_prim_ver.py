# 프림 알고리즘 사용. 시간 복잡도(e * log v) 간선에서 최소값을 꺼내는 과정이 logv이므로
import heapq


v, e = map(int, input().split())
edges = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

visited = set()
heap = [(0, 1)]
total_cost = 0

while heap:
    cost, u = heapq.heappop(heap)
    if u in visited:
        continue
    visited.add(u)
    total_cost += cost
    for v, w in edges[u]:
        if v not in visited:
            heapq.heappush(heap, (w, v))

print(total_cost)
