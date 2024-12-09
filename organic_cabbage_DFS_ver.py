import sys
# recursion 에러 대처 방안(python이 정한 최대 깊이를 변경함. )
sys.setrecursionlimit(10**6)

# 반복 횟수 입력
repeat = int(input())
# 결과 값 받을 곳 제작
result = []
# dfs 알고리즘 제작
def dfs(x, y):
  if (x < 0 or y < 0 or x >= n or y >= m):
    return False
  else:
    if (graph[x][y] == 1):
      graph[x][y] = 0
      dfs(x - 1, y)
      dfs(x + 1, y)
      dfs(x, y + 1)
      dfs(x, y - 1)
      return True

# 반복 시작
for _ in range(repeat):
  # 가로, 세로, 벌레 갯수 입력
  m, n, k = map(int, input().split())
  # 벌레 위치 입력
  graph = [[False] * (m) for _ in range(n)]
  for _ in range(k):
    y, x = map(int, input().split())
    graph[x][y] = True
  # 횟수 세기
  count = 0
  # 모든 위치를 탐색하면서, count 세기
  for y in range(m):
    for x in range(n):
      if dfs(x,y):
        count += 1
  result.append(count)
  
for i in result:
  print(i)