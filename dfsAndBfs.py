from collections import deque

n, m, v = map(int, input().split())

# 연결 여부 그래프 만들기 (양방향을 고려해서 제작)
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True
# 방문 여부 그래프 만들기
visited = [False] * (n + 1)


# dfs 함수 정의
def dfs(v):
  # 일단 방문하고 프린트
  visited[v] = True
  print(v, end=' ')
  # 모든 노드에 대해서 연결 여부를 확인해야 하므로, v 번째 연결 여부 그래프와 방문 여부를 확인함.
  for i in range(1, n + 1):
    # 만약 연결되어 있고, 방문되어 있지 않다면. dfs 실행
    if graph[v][i] and not visited[i]:
      dfs(i)


# bfs 함수 정의
def bfs(v):
  # 큐 구현, 미리 v 노드를 넣어놓음.
  queue = deque([v])
  # 큐에 넣었다면 방문했다고, 설정
  visited[v] = True
  while queue:
    # 큐에서 뺄 때, 프린트. 즉 방문하고 나옴.
    v = queue.popleft()
    print(v, end=' ')
    # dfs와 마찬가지로, 연결 여부 그래프와 방문 여부를 확인함.
    for i in range(1, n + 1):
      if (graph[v][i] and not visited[i]):
        queue.append(i)
        visited[i] = True


dfs(v)

# visited 초기화
visited = [False] * (n + 1)
print()
bfs(v)
