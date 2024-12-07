# 그룹이 2개가 될때까지 1년 씩 지나가면서 얼음을 녹여본다.
# 즉, 그룹을 세어보고, 얼음을 녹이고, 그룹을 세어보고 얼음을 녹이는 방식으로 이루어져야 함.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int, input().split()) 

ice= []

for _ in range(n):
    ice.append(list(map(int,input().split())))


# 상하좌우
dx =[-1,1,0,0]
dy = [0,0,-1,1] 


def count_group(x,y):
    count_iceberg[y][x]= 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if ice[ny][nx] == 0:
                count_iceberg[y][x] += 1
            elif ice[ny][nx] and count_iceberg[ny][nx] == 0:
                count_group(nx,ny)


cnt = 0

while True:
    # 빙하 주변의 바다를 세는 리스트
    count_iceberg = [[0]*m for _ in range(n)]
    # 빙하의 그룹 세는 변수
    cnt_group = 0

    # 먼저 바다의 그룹을 먼저 셈.
    for x in range(m):
        for y in range(n):
            if count_iceberg[y][x] ==0 and ice[y][x]:
                count_group(x,y)
                cnt_group += 1

    if cnt_group >=2:
        print(cnt)
        break
    elif cnt_group == 0:
        print(0)
        break


    # 빙하 녹이기
    for x in range(m):
        for y in range(n):
            if count_iceberg[y][x]:
                ice[y][x] -= (count_iceberg[y][x]-1)
                if ice[y][x] < 0:
                    ice[y][x] =0




    cnt += 1
    


    