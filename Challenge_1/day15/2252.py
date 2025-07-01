from collections import deque, defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 무엇에 연결되어 있는지 기록
    graph[a].append(b)
    # 진입 차수 기록
    in_degree[b] += 1

q = deque()
# 들어가는 게 없는 가장 우선순위가 높은 것부터 q에 넣기
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
result = []
# 연결되는 걸 하나씩 제거해가면서 우선순위 정하기
while q:
    idx = q.popleft()
    result.append(idx)
    for next_item in graph[idx]:
        in_degree[next_item] -= 1
        if in_degree[next_item] == 0:
            q.append(next_item)
print(*result)
