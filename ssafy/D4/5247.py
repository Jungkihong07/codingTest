from collections import deque


# import sys
#
# sys.stdin = open('sample_input.txt', 'r')


def solve(n, m):
    L = [999] * 1000001
    MAX = 1000000
    q = deque()
    q.append([n, 0])
    while q:
        current, cnt = q.popleft()
        if current == m:
            return cnt
        if 0 <= current + 1 <= MAX:
            if L[current + 1] == 999:
                L[current + 1] = cnt + 1
                q.append((current + 1, cnt + 1))
        if 0 <= current - 1 <= MAX:
            if L[current - 1] == 999:
                L[current - 1] = cnt + 1
                q.append((current - 1, cnt + 1))
        if 0 <= current * 2 <= MAX:
            if L[current * 2] == 999:
                L[current * 2] = cnt + 1
                q.append((current * 2, cnt + 1))
        if 0 <= current - 10 <= MAX:
            if L[current - 10] == 999:
                L[current - 10] = cnt + 1
                q.append((current - 10, cnt + 1))
    return -1


T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    print(f"#{t} {solve(n, m)}")
