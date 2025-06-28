# 시간 결과 2756 ms 걸림.
import sys
import heapq

# 최소 비용 구하기
n = int(input())  # 도시의 갯수
m = int(input())  # 간선의 갯수
weigth_board = [
    [0 if i == j else sys.maxsize for i in range(n + 1)] for j in range(n + 1)
]  # 도시 별 이동 가중치 기록

# 도시 별 이동 가중치 기록 2
for _ in range(m):
    start, end, weight = map(int, input().split())
    weigth_board[start][end] = min(weigth_board[start][end], weight)
# 출발지와 도착지 입력
start, end = map(int, input().split())
# 순서 대로 입력 (가중치, 출발지)
heap = []
heapq.heappush(heap, (0, start))
# 출발지 기준, 거리 계산
dist = [sys.maxsize] * (n + 1)
dist[start] = 0
visited = [False] * (n + 1)
visited[start] = True
while heap:
    cost, now = heapq.heappop(heap)
    for i in range(1, n + 1):
        if weigth_board[now][i] != sys.maxsize:
            dist[i] = min(dist[now] + weigth_board[now][i], dist[i])
            if not visited[i]:
                visited[i] = True
                heapq.heappush(heap, (dist[i], i))
print(dist[end])
