from collections import deque
import sys

WALL = '#'
SPACE = '.'

input = sys.stdin.readline

r,c = map(int, input().split())

maze =[]

for _ in range(r):
    maze.append(input().strip())
    
person = ''
fire = ''
px,py = 0,0
fx,fy = 0,0

# 사람의 위치와 불의 위치 파악
for x in range(r):
    for y in range(c):
        if person == '' or fire == '':
            if maze[y][x] == 'J':
                px,py = x,y
            elif maze[y][x] == 'F':
                fx,fy = x,y
        else:
            break

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solve_problem():
    visited = [[0]*c for _ in range(r)]
    fire_q = deque()
    fire_q.append((fx,fy))
    person_q = deque()
    person_q.append((px, py))
    visited[fy][fx] = 1
    visited[py][px] = 1
    while fire_q and person_q:
        frnx, frny = fire_q.popleft()
        prnx, prny = person_q.popleft()
        if (prnx == 0 ) or (prnx == (c-1)) or (prny == 0) or (prny == (r-1)):
            return cnt
        for i in range(4):
            pnx = prnx + dx[i]
            pny = prny + dy[i]
            if (0<= pnx < c) and (0<= pny < r) and maze[pny][pnx]=='.' and visited[pny][pnx]==0:
                person_q.append((pnx,pny))
                visited[pny][pnx] = visited[prny][prnx] + 1
                for i in range(4):
                    fnx = frnx  + dx[i]
                    fny = frny + dy[i]
                    if (0<= fnx < c) and (0<= fny < r) and maze[fny][fnx]=='.' and not visited[fny][fnx]:
                        fire_q.append((fnx,fny))
                        visited[fny][fnx] = True
                        break
    return False       
result = solve_problem()
if result:
    print(result)
else:
    print('IMPOSSIBLE')