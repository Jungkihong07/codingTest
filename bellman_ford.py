import sys
input = sys.stdin.readline
INF =int(1e9)
n,m = map(int,input().split())
edges =[]
dist= [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a,b,c))

def bf(start):
    dist[start] = 0
    # 전체 n번의 라운드 (round) 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1] 
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False

# 벨만 포드 알고리즘을 수행
negative_cycle = bf(1)  

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모드 노드로 가기 위한 최단 거리 출력
    for i in range(2,n+1):
        # 도달할 수 없는 경우, -1을 출력
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])