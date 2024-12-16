# 부녀회장이 될테야 문제
repeat = int(input())
results =[]
for _ in range(repeat):
    k = int(input())
    n = int(input())
    graph = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        graph[0][i] = i
    for i in range(1,k+1):
        for j in range(1,n+1):
            graph[i][j] = graph[i][j-1] + graph[i-1][j]
    results.append(graph[k][n])
for result in results:
    print(result)