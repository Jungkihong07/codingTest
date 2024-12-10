# 그룹이 2개가 될때까지 1년 씩 지나가면서 얼음을 녹여본다.
# 즉, 그룹을 세어보고, 얼음을 녹이고, 그룹을 세어보고 얼음을 녹이는 방식으로 이루어져야 함.
from collections import deque


n, m = map(int,input().split())

ice = [list(map(int,input().split())) for _ in range(n)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a,b):
    q = deque()
    q.append([a,b])
    visited[b][a] = 1
    sea_list = []
    while q:
        sea = 0
        rx,ry = q.popleft()
        for i in range(4):
            nx = rx + dx[i]
            ny = ry + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not ice[ny][nx]:
                    sea += 1
                elif ice[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([nx,ny])
        if sea > 0:
            sea_list.append((rx,ry,sea))
    for x,y,sea in sea_list:
        ice[y][x] = max(0, ice[y][x] - sea)

year = 0

while True:
    visited = [[0]*m for _ in range(n)]
    group = 0
    for x in range(m):
        for y in range(n):
            if not visited[y][x] and ice[y][x]:
                bfs(x,y)
                group += 1
    if group > 1:
        print(year)
        break
    elif not group:
        print(0)
        break
    year += 1
