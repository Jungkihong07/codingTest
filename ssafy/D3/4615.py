import sys

sys.stdin = open("sample_input.txt", 'r')

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, -1, 1, 1]


def solve(x, y, rock, board):
    board[y][x] = rock
    other_rock = 1 if rock == 2 else 2
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        flip_list = []
        while 1 <= nx <= n and 1 <= ny <= n and board[ny][nx] == other_rock:
            flip_list.append((nx, ny))
            nx += dx[d]
            ny += dy[d]
        if 1 <= nx <= n and 1 <= ny <= n and board[ny][nx] == rock:
            for fx, fy in flip_list:
                board[fy][fx] = rock
    return board


T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    center = n // 2
    board[center][center] = board[center + 1][center + 1] = 2
    board[center + 1][center] = board[center][center + 1] = 1

    for _ in range(m):
        x, y, rock = map(int, input().split())
        board = solve(x, y, rock, board)

    black_cnt = sum(row.count(1) for row in board)
    white_cnt = sum(row.count(2) for row in board)
    print(f"#{t} {white_cnt} {black_cnt}")

# 밑에 코드는 BFS를 활용하여 문제를 해결함. 하지만 문제 해석을 잘못했기에 오류가 남.print
# import sys
#
# sys.stdin = open("sample_input.txt", 'r')
# from collections import deque
#
#
# def solve(x, y, rock, board):
#     q = deque()
#     visited = set()
#     q.append((x, y, rock))
#     while q:
#         x, y, rock = q.popleft()
#         if (x, y) in visited:
#             continue
#         board[y][x] = rock
#         other_rock = 1 if rock == 2 else 2
#         cnt = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (1 <= nx <= n and 1 <= ny <= n) and board[ny][nx] == other_rock:
#                 cnt += 1
#         if cnt >= 2:
#             visited.add((x, y))
#             q.append((x, y, other_rock))
#             continue
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             add_list = []
#             while (1 <= nx <= n and 1 <= ny <= n) and board[ny][nx] == other_rock:
#                 add_list.append((nx, ny))
#                 nx += dx[i]
#                 ny += dy[i]
#             if (1 <= nx <= n and 1 <= ny <= n) and board[ny][nx] == rock:
#                 for col, row in add_list:
#                     visited.add((col, row))
#                     q.append((col, row, rock))
#         for i in range(2, 4):
#             for j in range(2):
#                 nx = x + dx[i]
#                 ny = y + dy[j]
#                 if (1 <= nx <= n and 1 <= ny <= n) and board[ny][nx] == rock:
#                     if board[ny][x] == other_rock:
#                         q.append((x, ny, rock))
#                     if board[y][nx] == other_rock:
#                         q.append((nx, y, rock))
#     return board
#
#
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# T = int(input())
# for t in range(1, T + 1):
#     n, m = map(int, input().split())
#     board = []
#     for _ in range(n + 1):
#         board.append([0] * (n + 1))
#     center = n // 2
#     board[center][center] = board[center + 1][center + 1] = 2
#     board[center + 1][center] = board[center][center + 1] = 1
#     for _ in range(m):
#         x, y, rock = map(int, input().split())
#         board = solve(x, y, rock, board)
#     black_cnt = 0
#     white_cnt = 0
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if board[i][j] == 1:
#                 black_cnt += 1
#             elif board[i][j] == 2:
#                 white_cnt += 1
#     print(f"#{t} {white_cnt} {black_cnt}")
