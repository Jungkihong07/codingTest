from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int,input().strip())))

# 상하좌우 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solve_problem():
    visited =[[[0]*2 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if x == m-1 and y == n-1:
            return visited[y][x][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                # 방문하지 않았고, 현지 위치에서 이동이 가능하다면
                if maze[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    q.append((nx,ny,z))
                elif maze[ny][nx] == 1 and z ==0:
                    visited[ny][nx][z+1] = visited[y][x][z] + 1
                    q.append([nx,ny,z+1])

    return -1

print(solve_problem())