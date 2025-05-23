import sys

sys.stdin = open('sample_input.txt', 'r')
from collections import deque


def bfs(board):
    visited = set()
    q = deque()
    for i in range(1, n + 1):
        q.append(([i], 1))
    max_num = 0
    while q:
        _list, num = q.popleft()
        is_end = True
        for i in range(1, n + 1):
            if i not in _list and board[_list[-1]][i]:
                is_end = False
                new_list = _list + [i]
                new_num = num + 1
                tuple_visited = tuple(new_list)
                if tuple_visited not in visited:
                    visited.add(tuple_visited)
                    q.append((new_list, new_num))
        if is_end:
            max_num = max(max_num, num)
    return max_num


T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        board[a][b] = True
        board[b][a] = True
    max_num = bfs(board)
    print(f"#{t} {max_num}")
