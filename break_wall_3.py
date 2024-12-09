import sys
from collections import deque


input = sys.stdin.readline

# 0의 갯수를 세고, 어디에 소속되어 있는지 기록하는 함수
def count_zero(x,y,cluster_num):
    global cluster
    q = deque()
    q.append((x,y))
    cluster[y][x] = cluster_num
    cnt = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if(0<=nx<m and 0 <= ny <n):
                if cluster[ny][nx]==0 and grid[ny][nx] == 0:
                    cluster[ny][nx] = cluster_num
                    q.append((nx,ny))
                    cnt += 1
    return cnt

n,m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().strip())))
# 각 클래스터 그룹 번호 = 인덱스 기준 , 0의 갯수 기록
cluster_record = [0]
# 클러스터 넘버링
cluster_num = 1
# 그리드로 클러스트 그룹별 번호 기록 
cluster =  [[0]*m for _ in range(n)]

# 상하좌우 설정
dx = [-1,1,0,0]
dy =  [0,0,-1,1]

# 0의 갯수를 세고, 어느 클러스터에 소속되어 있지 않다면 진행.
for x in range(m):
    for y in range(n):
        if grid[y][x] == 0 and cluster[y][x] == 0 :
            cnt_zero = count_zero(x,y,cluster_num)
            cluster_record.append(cnt_zero%10)
            cluster_num += 1


# 클러스터 그룹과 1을 부쉈을 때를 기준으로, grid를 새로 업데이트
for x in range(m):
    for y in range(n):
        if grid[y][x] == 1:
            cluster_grid = set()
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if (0<=nx<m and 0 <= ny <n):
                    cluster_grid.add(cluster[ny][nx])
            for i in cluster_grid:
                grid[y][x]+= cluster_record[i]
            grid[y][x] %= 10

for y in grid:
    for x in y:
        print(x, end='')
    print()






        
    

