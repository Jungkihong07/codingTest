# 해당 문제는 전체적으로 조사를 하면서 나아갈 수 밖에 없었음. 그냥 귀찮게 까다로웠다는 말... momory까지 고려해서 짜야 했으니...
from collections import deque

# 방향: ↑ ↓ ← →
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solve(R: int, C: int, board: list):
    visited = [[[[False] * 16 for _ in range(4)] for _ in range(C)] for _ in range(R)]
    queue = deque()
    queue.append((0, 0, 0, 3))  # y, x, memory, direction

    while queue:
        y, x, mem, d = queue.popleft()
        if visited[y][x][d][mem]:
            continue
        visited[y][x][d][mem] = True

        char = board[y][x]
        if char == "@":
            return "YES"
        elif char == ">":
            d = 3
        elif char == "<":
            d = 2
        elif char == "^":
            d = 0
        elif char == "v":
            d = 1
        elif char == "_":
            d = 3 if mem == 0 else 2
        elif char == "|":
            d = 1 if mem == 0 else 0
        elif char == "?":
            for nd in range(4):
                ny = (y + dy[nd]) % R
                nx = (x + dx[nd]) % C
                queue.append((ny, nx, mem, nd))
            continue
        elif char == "+":
            mem = (mem + 1) % 16
        elif char == "-":
            mem = (mem - 1) % 16
        elif char.isdigit():
            mem = int(char)

        ny = (y + dy[d]) % R
        nx = (x + dx[d]) % C
        queue.append((ny, nx, mem, d))

    return "NO"


T = int(input())
for i in range(1, T + 1):
    r, c = map(int, input().split())
    board = []
    for _ in range(r):
        board.append(list(map(str, input().strip())))
    print(f"#{i} {solve( r,c,board)}")
