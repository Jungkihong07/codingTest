def move(person, y, x):
    opened = [[False] * n for _ in range(n)]
    cnt = 0
    stack = [(y, x)]
    total = 0
    while stack:
        y, x = stack.pop()
        opened[y][x] = True
        cnt += 1
        total += person[y][x]
        for d in range(4):
            ax = x + dx[d]
            ay = y + dy[d]
            if 0 <= ax < n and 0 <= ay < n and not opened[ay][ax]:
                if l <= abs(person[y][x] - person[ay][ax]) <= r:
                    stack.append((ay, ax))

    popular = int(total / cnt)
    for row in range(n):
        for col in range(n):
            if opened[row][col]:
                person[row][col] = popular


n, l, r = map(int, input().split())
person = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

day = 0
while 1:
    day += 1
    moved = True
    for row in range(n):
        for col in range(n):
            is_opened = False
            for d in range(4):
                ar = row + dy[d]
                ac = col + dx[d]
                if 0 <= ar < n and 0 <= ac < n:
                    if l <= abs(person[row][col] - person[ar][ac]) <= r:
                        is_opened = True
                        break
            if is_opened:
                moved = True
                move(person, row, col)
    if not moved:
        break
    
print(day)
