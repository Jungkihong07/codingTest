# [백준] 1865번 웜홀 실패 코드(이유: 시간 복잡도가 너무 큼) + 문제 해결
import sys
input = sys.stdin.readline

tc = int(input())

INF= int(1e9)

def solve():
    graph[1] = 0
    for i in range(n):
        for j in edges:
            now = j[0]
            end = j[1]
            dist = j[2]
            if graph[now] != INF and graph[end] > graph[now] + dist:
                graph[end] = graph[now] + dist
                if i == n-1:
                    return True
    return False

result = []
for _ in range(tc):
    n,m,w = map(int,input().split())
    graph = [INF] * (n+1)
    edges = []
    for _ in range(m):
        s,e,t = map(int,input().split())
        edges.append([s,e,t])
        edges.append([e,s,t])
    for _ in range(w):
        s,e,t = map(int,input().split())
        edges.append([s,e,-t])
    result.append(solve())

for a in result:
    print("YES" if a else "NO")  


# def solve():
#     for a in range(1, n+1):
#         for start in range(1, n+1):
#             for end in range(1, n+1):
#                 graph[start][end] = min(graph[start][end], graph[start][a]+ graph[a][end])
#                 if  (graph[start][end] + graph[end][start]) < 0:
#                     return True
#     return False

# result = []
# for _ in range(tc):
#     n,m,w = map(int,input().split())
#     graph =[[INF]*(n+1) for _ in range(n+1)]
#     for _ in range(m):
#         s,e,t = map(int,input().split())
#         graph[s][e] = t
#         graph[e][s] = t
#     for i in range(1,n+1):
#         graph[i][i] = 0
#     for _ in range(w):
#         s,e,t = map(int,input().split())
#         if graph[s][e] == INF:
#             graph[s][e] = -t
#         else:
#             graph[s][e] -= t
#     result.append(solve())