# 크루스칼 알고리즘 사용. 시간 복잡도 O(eloge) => 간선 정렬로 인한 시간이 오래 걸림.
import sys

sys.setrecursionlimit(10**6)


v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])

parent = list(range(v + 1))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    parent_a, parent_b = find(a), find(b)
    if parent_a != parent_b:
        parent[parent_b] = parent_a
        return True
    return False


result = 0
for s, e, w in edges:
    if union(s, e):
        result += w
print(result)
