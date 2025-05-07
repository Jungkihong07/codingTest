# 주의할 점. 방향 파악 부분 + 각 부분에 예외적인 부분 파악.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]  # 북, 동, 남, 서 순으로 재배치 (인덱스 0이 북쪽이 되도록)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[2 if is_cleaned else 0 for is_cleaned in line] for line in room]
stack = [(r, c, d)]
while stack:
    y, x, d = stack.pop()
    if not cleaned[y][x]:
        cleaned[y][x] = 1
    all_cleaned = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not cleaned[ny][nx]:
            all_cleaned = False
            break
    if all_cleaned:
        ax = x + dx[(d + 2) % 4]
        ay = y + dy[(d + 2) % 4]
        if 0 <= ay < n and 0 <= ax < m and cleaned[ay][ax] != 2:
            stack.append((ay, ax, d))
        else:
            break
    else:
        d = (d - 1) % 4
        ax = x + dx[d]
        ay = y + dy[d]
        if 0 <= ay < n and 0 <= ax < m and not cleaned[ay][ax]:
            stack.append((ay, ax, d))
        else:
            stack.append((y, x, d))
result = 0
for i in cleaned:
    for is_cleand in i:
        if is_cleand == 1:
            result += 1
print(result)
