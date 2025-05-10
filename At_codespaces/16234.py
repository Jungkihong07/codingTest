from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def move(visited, c_row, c_col):
    q = deque([(c_row, c_col)])
    visited[c_row][c_col] = True
    union = [(c_row, c_col)]
    total = 0
    while q:
        row, col = q.popleft()
        total += people[row][col]
        for d in range(4):
            d_row = row + dr[d]
            d_col = col + dc[d]
            if 0 <= d_row < n and 0 <= d_col < n:
                if not visited[d_row][d_col]:
                    if l <= abs(people[row][col] - people[d_row][d_col]) <= r:
                        q.append((d_row, d_col))
                        visited[d_row][d_col] = True
                        union.append((d_row, d_col))
    result_people = total // len(union)
    if len(union) > 1:
        for row, col in union:
            people[row][col] = result_people
        return True
    return False


n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]

day = 0

while 1:
    moved = False
    visited = [[False] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                if move(visited, row, col):
                    moved = True
    if not moved:
        break
    day += 1
print(day)
