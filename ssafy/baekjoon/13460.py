from collections import deque

dx = [0, 0, -1, 1]  # 좌우상하
dy = [-1, 1, 0, 0]


def move(x, y, dx, dy, board):
    cnt = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(board, rx, ry, bx, by):
    visited = set()
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited.add((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            return -1

        for i in range(4):
            nrx, nry, r_cnt = move(rx, ry, dx[i], dy[i], board)
            nbx, nby, b_cnt = move(bx, by, dx[i], dy[i], board)

            if board[nby][nbx] == 'O':
                continue  # 파란 구슬이 구멍에 빠지면 실패
            if board[nry][nrx] == 'O':
                return depth  # 빨간 구슬만 빠졌을 때 성공

            if nrx == nbx and nry == nby:
                # 구슬이 같은 위치에 있을 수 없으므로, 더 많이 움직인 쪽을 한 칸 뒤로
                if r_cnt > b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1


n, m = map(int, input().split())
board = []
for i in range(n):
    row = list(input().strip())
    board.append(row)
    for j in range(m):
        if row[j] == 'R':
            rx, ry = j, i
        elif row[j] == 'B':
            bx, by = j, i

print(bfs(board, rx, ry, bx, by))
