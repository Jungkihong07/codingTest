from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int, input().split())

maze =[]

for _ in range(r):
    maze.append(list(input().strip()))
    
fire_location=[]

# 사람의 위치와 불의 위치 파악
for x in range(c):
    for y in range(r):
        if maze[y][x] == 'J':
            px,py = x,y
        elif maze[y][x] == 'F':
            fx,fy = x,y
            fire_location.append((fx,fy))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solve_problem():
    global fire_location
    visited = [[0]*c for _ in range(r)]
    for x,y in fire_location:
        visited[y][x] = -1
    person_q = deque()
    person_q.append((px, py))
    visited[py][px] = 1
    while person_q:
        # 그 외의 모든 불들이 확산됨.
        fire_location_ex = []
        for x,y in fire_location:
            frnx , frny = x,y
            for i in range(4):
                fnx = frnx  + dx[i]
                fny = frny + dy[i]
                if (0<= fnx < c) and (0<= fny < r) and maze[fny][fnx]=='.' and visited[fny][fnx] == 0:
                    fire_location_ex.append((fnx,fny))
                    visited[fny][fnx] = -1
        # 확산된 불들이 다음에 더 넘어갈 수 있으므로 교체
        fire_location= fire_location_ex
        # 사람이 먼저 한 발짝 감.
        prnx, prny = person_q.popleft()
        if (prnx == 0) or (prnx == (c-1)) or (prny == 0) or (prny == (r-1)):
            return visited[prny][prnx]
        for i in range(4):
            pnx = prnx + dx[i]
            pny = prny + dy[i]
            if (0<= pnx < c) and (0<= pny < r) and maze[pny][pnx]=='.' and visited[pny][pnx]==0:
                person_q.append((pnx,pny))
                visited[pny][pnx] = visited[prny][prnx] + 1

    return False       
result = solve_problem()
if result:
    print(result)
else:
    print('IMPOSSIBLE')