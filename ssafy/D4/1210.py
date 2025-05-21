from collections import deque
import sys

sys.stdin = open("input.txt", "r")

dx = [1, -1, 0]
dy = [0, 0, -1]


def solve(start_r, start_c, board):
    q = deque()
    q.append([start_c, start_r, 0])
    while q:
        x, y, d = q.popleft()
        if y == 0:
            return x
        if d == 2:
            for i in range(3):
                rx = x + dx[i]
                ry = y + dy[i]
                if 0 <= rx < 100 and 0 <= ry < 100:
                    if board[ry][rx] == 1:
                        q.append((rx, ry, i))
                        break
        elif d == 1:
            for i in [2, 1]:
                rx = x + dx[i]
                ry = y + dy[i]
                if 0 <= rx < 100 and 0 <= ry < 100:
                    if board[ry][rx] == 1:
                        q.append((rx, ry, i))
                        break
        elif d == 0:
            for i in [2, 0]:
                rx = x + dx[i]
                ry = y + dy[i]
                if 0 <= rx < 100 and 0 <= ry < 100:
                    if board[ry][rx] == 1:
                        q.append((rx, ry, i))
                        break
    return -1


for _ in range(10):
    t = int(input())
    board = []
    for r in range(100):
        _list = list(map(int, input().split()))
        board.append(_list)
        for c in range(100):
            if _list[c] == 2:
                start_r = r
                start_c = c
    print(f"#{t} {solve(start_r, start_c, board)}")
