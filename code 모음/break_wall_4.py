import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int, input().strip())))

cluster_num = 1

# 상하좌우 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 클러스터 소속 기록
cluster_grid = [[0]*m for _ in range(n)]
# 클러스터 그룹 별 가지고 있는 0 갯수 기록
cluster_record =[0]

def bfs(x,y):
    global cluster_grid
    q = deque()
    q.append((x,y))
    cnt = 1
    # 처음 들어왔을 때, 클러스터에 소속되기 때문.
    cluster_grid[y][x] = cluster_num
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            if (0<=nx<m) and (0<=ny<n):
                # (아무 클러스터에 소속되어 있지 않다 == 방문하지 않았다) and (갈 수 있는 길일 경우)
                if cluster_grid[ny][nx] == 0 and grid[ny][nx] == 0 :
                    q.append((nx,ny))
                    cluster_grid[ny][nx] = cluster_num
                    cnt+= 1
    return cnt

for y in range(n):
    for x in range(m):
        if grid[y][x] == 0 and cluster_grid[y][x] == 0:
            # 클러스터 보유 0의 개수 기록과 클러스터 넘버링
            cluster_record.append(bfs(x,y))
            cluster_num += 1

def zero_count(x,y):
    size = len(cluster_record)
    count = 0
    visited = [False] * size
    for i in range(1,size):
        for j in range(4):
            nx = x +dx[j]
            ny = y + dy[j]
            if (0<=nx<m) and (0<=ny<n):
                if cluster_grid[ny][nx] == i and not visited[i]:
                    visited[i] = True
                    count += cluster_record[i]
    return count%10

    


for y in range(n):
    for x in range(m):
        if grid[y][x] == 1:
           grid[y][x] = zero_count(x,y) + 1

for i in grid:
    for j in i:
        print(j,end='')
    print()