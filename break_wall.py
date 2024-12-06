# 해당 코드 다시 작성할 것.!!!

from collections import deque

n, m = map(int, input().split())

maze =  []
for _ in range(n):
    maze.append(list(map(int, input())))

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a,b):
    q = deque([(a,b)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 and ny <0 and nx >= n and ny >= y:
                continue
                