from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
  maze.append(list(map(int, input())))

# 상하좌우 나타내기
dx = [-1,1, 0, 0]
dy = [0,0,-1,1]

def solve(x,y):
  queue = deque()
  queue.append((x,y))
  # 큐가 빌 때까지 반복하기
  while queue:
    x,y = queue.popleft()
    # 상하좌우 다녀오기
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 만약 벗어나면 무시하기
      if nx < 0 or ny <0 or nx >=n or ny >=m:
        continue
      # 만약 벽이면 무시하기
      if maze[nx][ny] == 0:
        continue
      # 만약 갈 수 있는 길이면 최단 거리 기록하기
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx,ny))
  # 도착한 최단 거리 출력하기
  return maze[n-1][m-1]

print(solve(0,0))