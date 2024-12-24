# [백준] 1781번 컵라면
import heapq
import sys

input = sys.stdin.readline

n = int(input())
# 정보를 담아놓을 리스트
array = []

for i in range(1,n+1):
    d,c = map(int,input().split())
    array.append((d,c))
array.sort()

q = []
for i in array:
    heapq.heappush(q,i[1])
    # 데드라인을 넘어선 문제는 빼낸다.
    if i[0] < len(q):
        heapq.heappop(q)
print(sum(q))




