from collections import deque

n,m = map(int, input().split())
# 최대 크기 만큼 생성
MAX = 10**5
# 방문 리스트 생성
visited = [0]*(MAX + 1)
# 최초로 방문한 횟수가 곧 최소 방문 횟수이므로, 가장 먼저 방문할 수 있도록만 고려하기.
def bfs(n):
    q = deque([n])
    while q:
        a = q.popleft()
        # 만약 a가 m에 도달했다면, 멈춤
        if (a == m):
            return visited[a]
        for i in (a-1 , a+1, a*2):
            if (0 <= i <= MAX) and not visited[i]:
                visited[i] = visited[a] + 1
                q.append(i)
print(bfs(n))
        
    