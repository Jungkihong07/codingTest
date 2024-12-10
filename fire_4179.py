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
    visited_f = [[0]*c for _ in range(r)]
    visited_j = [[0]*c for _ in range(r)]
    person_q = deque()
    fire_q = deque()
    for x,y in fire_location:
        fire_q.append([x,y])
        visited_f[y][x] = 1
    person_q.append((px, py))
    visited_j[py][px] = 1

    # 불에 대해서 먼저 기록
    while fire_q:
        prnx, prny = fire_q.popleft()
        for i in range(4):
            pnx = prnx + dx[i]
            pny = prny + dy[i]
            if (0<= pnx < c) and (0<= pny < r) and maze[pny][pnx]=='.' and not visited_f[pny][pnx]:
                fire_q.append((pnx,pny))
                visited_f[pny][pnx] = visited_f[prny][prnx] + 1
    # 사람에 대해서 먼저 기록
    while person_q:
        prnx, prny = person_q.popleft()
        if (prnx == 0) or (prnx == (c-1)) or (prny == 0) or (prny == (r-1)):
            return visited_j[prny][prnx]
        for i in range(4):
            pnx = prnx + dx[i]
            pny = prny + dy[i]
            if (0<= pnx < c) and (0<= pny < r) and maze[pny][pnx]=='.' and not visited_j[pny][pnx]:
                if (visited_f[pny][pnx] and visited_f[pny][pnx]>visited_j[prny][prnx]+1) or not visited_f[pny][pnx]:
                    person_q.append((pnx,pny))
                    visited_j[pny][pnx] = visited_j[prny][prnx] + 1

    return False       
result = solve_problem()
if result:
    print(result)
else:
    print('IMPOSSIBLE')