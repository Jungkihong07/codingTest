from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board):
    q = deque()
    visited = set()
    visited.add((1, 1))
    q.append((1, 1, 1))
    while q:
        x, y, depth = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 1 <= nx <= m and 1 <= ny <= n:
                if nx == m and ny == n:
                    return depth + 1
                if board[ny][nx]:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny, depth + 1))
    return -1


n, m = map(int, input().split())
board = [[0]]
for _ in range(n):
    board.append([0] + list(map(int, input().strip())))
print(bfs(board))
