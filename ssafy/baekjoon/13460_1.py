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


def solve(board, rx, ry, bx, by):
    visited = set()
    q = deque()
    q.append([rx, ry, bx, by, 1])
    visited.add(((rx, ry, bx, by)))
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            return -1

        for i in range(4):
            nrx, nry, r_cnt = move(rx, ry, dx[i], dy[i], board)
            nbx, nby, b_cnt = move(bx, by, dx[i], dy[i], board)

            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                return depth

            if nbx == nrx and nby == nry:
                if r_cnt < b_cnt:
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))
    return -1


n, m = map(int, input().split())
board = []
for j in range(n):
    _list = list(input().strip())
    board.append(_list)
    for i in range(m):
        if _list[i] == 'R':
            rx, ry = i, j
        if _list[i] == 'B':
            bx, by = i, j
# 결과 출력
print(solve(board, rx, ry, bx, by))
