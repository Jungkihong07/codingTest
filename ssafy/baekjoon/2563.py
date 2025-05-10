t = int(input())
board = [[0] * 100 for _ in range(100)]
for _ in range(t):
    x, y = map(int, input().split())
    for row in range(y, y + 10):
        for col in range(x, x + 10):
            board[row][col] = 1
result = 0
for i in range(100):
    result += sum(board[i])
print(result)
