# 못 풀겠다 꾀고리. ㅠ 다시 천천히 해보자.

dx = [1, 0, 0, -1]  # 차례대로 우, 위, 아래, 좌
dy = [0, 1, -1, 0]


def changed_postion(x, y, current_x, current_y):
    temp = board[current_y][current_x]
    board[current_y][current_x] = board[y][x]
    board[y][x] = temp


def move(direct, x, y, board):
    while board[y][x] != "#":
        ax = x + dx[direct]
        ay = y + dy[direct]
        if board[ay][ax] != "#":
            changed_postion(x, y, ax, ay)
            x = ax
            y = ay


def solve(board, n, m):
    cnt = 0
    # while 1:
    #     for direct in range(4):
    pass


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input().split())))
