# 위상 정렬 알고리즘

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 a에서 b로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소의 연결된 노드들의 진입차수에서 1을 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=" ")


topology_sort()
