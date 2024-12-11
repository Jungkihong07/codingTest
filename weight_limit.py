import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

start, end = map(int,input().split())


def bfs(mid):
    visited =[False for _ in range(n+1)]
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        if a == end:
            return True
        for i in graph[a]:
            if not visited[i[0]] and mid <= i[1]:
                visited[i[0]] = True
                q.append(i[0])
    return False

min, weight = 1,1000000000

while(min <= weight):
    mid = (min+ weight) //2 or 1
    if bfs(mid):
        min = mid + 1
    else:
        weight = mid - 1

print(weight)