# 아 너무 너무 어려워요.ㅠ
import sys

sys.stdin = open('sample_input.txt', 'r')


def solve(N):
    count = 0
    stack = []
    row = 0
    board = [-1] * N
    while True:
        found = False
        for col in range(board[row] + 1, N):
            safe = True
            for r in range(row):
                if board[r] == col or abs(board[r] - col) == abs(r - row):
                    safe = False
                    break
            if safe:
                board[row] = col
                stack.append((row, col))
                row += 1
                found = True
                break
        if not found:
            board[row] = -1
            if not stack:
                break
            row, prev_col = stack.pop()
        if row == N:
            count += 1
            row, prev_col = stack.pop()
            board[row] = prev_col
    return count


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = solve(N)
    print(f"#{t} {result}")
