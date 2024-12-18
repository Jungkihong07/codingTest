# [백준] 1865번 웜홀 실패 코드(이유: 시간 복잡도가 너무 큼)
import sys
input = sys.stdin.readline

tc = int(input())

INF= int(1e9)

def solve():
    for node in range(n):
        for cur,next_node,cost in line:
            if graph[next_node] > graph[cur] + cost:
                graph[next_node] = graph[cur] + cost
                if node == n-1:
                    return True
    return False 
result =[]

for _ in range(tc):
    n,m,w = map(int,input().split())
    line = []
    graph =[INF] *(n+1)
    for _ in range(m):
        s,e,t = map(int,input().split())
        line.append((s,e,t))
        line.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        line.append((s,e,-t))
    
    go = solve(1)
    result.append(go)

for i in result:
    print("YES" if i else "NO")