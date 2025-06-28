import sys
from collections import deque


# 최소 비용 구하기
n = int(input())
m = int(input())
weigth_board = [
    [0 if i == j else sys.maxsize for i in range(n + 1)] for j in range(n + 1)
]
for _ in range(m):
    start, end, weight = map(int, input().split())
    weigth_board[start][end] = min(weigth_board[start][end], weight)
start, end = map(int, input().split())

q = deque()
q.append(start)
start_board = [sys.maxsize] * (n + 1)
visited = [False] * (n + 1)
visited[start] = True
start_board[start] = 0

while q:
    next_node = q.popleft()
    for i in range(1, n + 1):
        if weigth_board[next_node][i] != sys.maxsize and weigth_board[next_node][i]:
            start_board[i] = min(
                start_board[next_node] + weigth_board[next_node][i], start_board[i]
            )
            if not visited[i]:
                visited[i] = True
                q.append(i)
print(start_board[end])
