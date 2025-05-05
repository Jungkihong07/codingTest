from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
  maze.append(list(map(int, input())))

# 이동 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  # queue가 다 비워질 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 4가지 방향으로 이동
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 벗어나는 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 벽인 경우 무시
      if maze[nx][ny] == 0:
        continue
      # 갈 수 있는 길이라면 추가
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))
  # 가장 마지막에 거리를 출력
  print(maze[n - 1][m - 1])


bfs(0, 0)
