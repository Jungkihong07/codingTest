import sys

sys.stdin = open('sample_input.txt', 'r')

dx = [1, 1, 0, -1]  # 오른쪽, 대각선 오른쪽 아래, 아래, 대각선 왼쪽 아래
dy = [0, 1, 1, 1]


def solve(board):
    for row in range(n):
        for col in range(n):
            for i in range(4):
                nx = col
                ny = row
                cnt = 0
                while 0 <= nx < n and 0 <= ny < n and cnt < 5:
                    if board[ny][nx] == 'o':
                        cnt += 1
                    else:
                        break
                    nx += dx[i]
                    ny += dy[i]
                if cnt == 5:
                    return True

    return False


# def solve(board):
#     for row in range(n):
#         for col in range(n):
#             for i in range(4):
#                 cnt = 0
#                 for k in range(5):  # 정확히 5칸만 확인
#                     ny = row + dy[i] * k
#                     nx = col + dx[i] * k
#                     if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 'o':
#                         cnt += 1
#                     else:
#                         break
#                 if cnt == 5:
#                     return True
#     return False


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(str, input().strip())) for _ in range(n)]
    result = "YES" if solve(board) else "NO"
    print(f"#{t} {result}")
