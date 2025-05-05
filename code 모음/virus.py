n = int(input())
m = int(input())

# 연결 기록 그래프 제작
graph = [[False] * (n + 1) for _ in range(n + 1)]

# 연결 기록 작성
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

# 감염 기록 작성
infection = [False] * (n + 1)

# 1부터 감염시키면서 시작하므로 -1에서 count 시작
count = -1


def bfs(v):
  global count
  infection[v] = True
  count += 1
  for i in range(1, n + 1):
    if graph[v][i] and not infection[i]:
      bfs(i)


bfs(1)
print(count)
