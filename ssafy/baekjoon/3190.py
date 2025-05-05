# 아직 못 풀음.

dx = [0, 0, 1, -1]  # 상 하 우 좌 0 1 2 3
dy = [1, -1, 0, 0]


def is_ahead(ahead, c):
    if c == "L":
        pass
    pass


def change(x, y, c_x, c_y):
    temp = board[y][x]
    board[y][x] = board[c_y][c_x]
    board[c_y][c_x] = temp


def move(tail_x, tail_y, head_x, head_y, x, c, board):
    for i in range(x):
        c_x = x + dx


N = int(input())
k = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(k):
    x, y = map(int, input().split())
    board[y - 1][x - 1] = 1


L = int(input())
head_x, head_y, tail_x, tail_y = 0
ahead = 2
for _ in range(L):
    x, c = map(str, input().split())
    x = int(x)
