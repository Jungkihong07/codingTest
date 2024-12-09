n, m = map(int, input().split())

juice = []
for _ in range(n):
  juice.append(list(map(int, input())))

result = 0

def dfs(a,b):
  # 만약 벗어나면 그만두기
  if a <= -1 or b <= -1 or a >= n or b >= m:
    return False
  # 만약 벗어나지 않고, 방문할 수 있다면
  if juice[a][b] == 0:
    juice[a][b] = 1
    dfs(a-1,b)
    dfs(a+1,b)
    dfs(a,b-1)
    dfs(a,b+1)
    return True 
  return False



for i in range(n):
  for j in range(m):
    # 하나의 사이클이 되었다면 result 하나 추가
    if dfs(i,j) == True:
      result  += 1
print(result)