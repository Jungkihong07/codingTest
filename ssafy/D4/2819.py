# 해당 문제 해결 완료. BFS가 조금 낮설다. 조금만 더 익숙해져보자. ,  dfs랑은 일반 스택을 이용해서, 빼는 순서만 다름.
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(board: list, x, y, result: set):
    s: str = str(board[y][x])
    q = deque([(x, y, s)])
    while q:
        x, y, s = q.popleft()
        if len(s) == 7:
            result.add(s)
            continue
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < 4 and 0 <= ay < 4:
                new_item = s + str(board[ay][ax])
                q.append((ax, ay, new_item))


def solve(board: list):
    result = set()
    for x in range(4):
        for y in range(4):
            move(board, x, y, result)
    return len(result)


T = int(input())
for i in range(1, T + 1):
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))
    print(f"#{i} {solve(board)}")
