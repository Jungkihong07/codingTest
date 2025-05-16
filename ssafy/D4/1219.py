from collections import deque


def solve(map_1: list):
    visited = [False] * 100
    visited[0] = True
    q = deque()
    q.append(0)
    is_true = False
    while q:

        start = q.popleft()
        if start == 99:
            is_true = True
            return is_true
        for dst in map_1[start]:
            if not visited[dst]:
                visited[dst] = True
                q.append(dst)
    return is_true


for i in range(10):
    N, L = map(int, input().split())
    map_1 = [[] for _ in range(100)]
    _list = list(map(int, input().split()))
    for j in range(0, L * 2, 2):
        map_1[_list[j]].append(_list[j + 1])
    print(f"#{i} {1 if solve(map_1) else 0}")
