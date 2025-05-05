# 으어 아직 잘 모르겠다. 나중에 다시 풀자. 지금은 조금 쉬운걸로 풀어보자.


from copy import deepcopy

t = int(input())

# 전선 방향 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def is_valid(x, y, dir, board):
    length = 0
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or y < 0 or x >= N or y >= N:
            return length
        if board[y][x] != 0:
            return 0
        length += 1


def set_line(x, y, dir, board):
    x_, y_ = x, y
    while True:
        x_ += dx[dir]
        y_ += dy[dir]
        if x_ < 0 or y_ < 0 or x_ >= N or y_ >= N:
            break
        board[y_][x_] = 2  # 2로 표시(전선)


# connected : 현재까지 연결한 core 수 / current : 현재 몇 번째 core를 처리하고 있는가?
def solve(current, connected, length, board):
    global max_connected, min_length
    if current == len(core_list):
        if connected > max_connected:
            max_connected = connected
            min_length = length
        elif connected == max_connected:
            min_length = min(min_length, length)
        return

    x, y = core_list[current]

    for dir in range(4):
        l = is_valid(x, y, dir, board)
        if l:
            b_copy = deepcopy(board)
            set_line(x, y, dir, b_copy)
            solve(current + 1, connected + 1, length + l, b_copy)

    solve(current + 1, connected, length, board)


for i in range(1, t + 1):
    N = int(input())
    _list = []
    for _ in range(N):
        _list.append(list(map(int, input().split())))
    core_list = []

    for x in range(1, N - 1):
        for y in range(1, N - 1):
            if _list[y][x] == 1:
                core_list.append((x, y))
    max_connected = -1
    min_length = float("inf")

    solve(0, 0, 0, _list)

    print(f"#{i} {min_length}")
