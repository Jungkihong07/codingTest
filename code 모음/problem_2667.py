from collections import deque
import heapq
import sys

input = sys.stdin.readline

s = int(input())
array = []
for _ in range(s):
    array.append(list(map(int,input().strip())))

visited = [[0]*s for _ in range(s)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

num = 0

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append([x,y])
    visited[y][x] = num
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0 <= nx < s and 0 <= ny < s:
                if array[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = num
                    cnt += 1
                    q.append([nx,ny])
    return cnt
result = []

for x in range(s):
    for y in range(s):
        if not visited[y][x] and array[y][x]:
            num += 1
            heapq.heappush(result,bfs(x,y))
print(num)
result.sort()
for a in result:
    print(a)