n = int(input())
zone = [[] * n for _ in range(n)]
sink_zone = zone.copy()
for i in range(n):
  zone[i] = list(map(int, input().split()))


def solve_dfs(x, y, depth):
  if x < 0 or y < 0 or x >= n or y >= n:
    return 0
  elif sink_zone[x][y] > depth:
    solve_dfs(x - 1, y, depth)
    solve_dfs(x + 1, y, depth)
    solve_dfs(x, y - 1, depth)
    solve_dfs(x, y + 1, depth)
    sink_zone[x][y] = depth
  return 1


max_safe_zone = 0

for depth in range(1,n):
  safe_zone = 0
  for i in range(n):
    for j in range(n):
      safe_zone += solve_dfs(i, j, depth)
  if safe_zone > max_safe_zone:
    max_safe_zone = safe_zone
  else:
    break
print(max_safe_zone)
