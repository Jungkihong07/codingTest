# [백준] 7576번 토마토
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

array = []
for _ in range(m):
    array.append(list(map(int,input().split())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]

q= deque()

def bfs():
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[ny][nx] == 0: 
                    array[ny][nx] = array[ay][ax] + 1
                    q.append([nx,ny])

for x in range(n):
    for y in range(m):
        if array[y][x] == 1:
            q.append([x,y])

bfs()

day = 0

for line in array:
    for item in line:
        if not item:
            print(-1)
            exit()
    day = max(day, max(line))

print(day-1)
