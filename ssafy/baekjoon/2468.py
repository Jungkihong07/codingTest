from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solve(x, y, board, visited, day):
    q = deque()
    q.append([x, y])
    visited[y][x] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] != 1 and board[ny][nx] > day:
                    visited[ny][nx] = 1
                    q.append([nx, ny])
                elif board[ny][nx] <= day:
                    visited[ny][nx] = 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
safe_zone = set()
day = 0
while day <= 100:
    zone = 0
    visited = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[y][x] > day and not visited[y][x]:
                solve(x, y, board, visited, day)
                zone += 1
            else:
                visited[y][x] = 1
    safe_zone.add(zone)
    day += 1

print(max(safe_zone))
