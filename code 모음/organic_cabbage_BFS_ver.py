from collections import deque

# 반복 횟수 입력
repeat = int(input())
# 결과 값 받을 곳 제작
result = []

# 이동 위치 확인하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 알고리즘 제작
def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  # 인접한 모든 배추를 방문한 것으로 간주하고 모두 false로 초기화
  graph[y][x] = False
  while queue:
    a,b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (nx <0 or ny <0 or nx >=m or ny >=n):
        continue
      if graph[ny][nx]:
        queue.append((nx,ny))
        graph[ny][nx] = False
  # 한 번 사이클을 돈 것이므로 1 return
  return 1

# 반복 시작
for _ in range(repeat):
  # 가로, 세로, 벌레 갯수 입력
  m, n, k = map(int, input().split())
  # 벌레 위치 입력
  graph = [[False] * (m) for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = True
  # 횟수 세기
  count = 0
  # 모든 위치를 탐색하면서, 사이클 세기
  for x in range(m):
    for y in range(n):
      if graph[y][x]:
        count += bfs(x,y)
  result.append(count)

for i in result:
  print(i)