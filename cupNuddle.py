# 해당 문제는 우선 순위 큐를 해결하고 나서 하는 걸로 하자.
import sys

input= sys.stdin.readline
n = int(input())

deadline=[[] for _ in range(n+1)]

for i in range(1,n+1):
    t, cup = map(int,input().split())
    deadline[t].append([i,cup])

for a in deadline:
    # 컵을 기준으로 재정렬
    a.sort(reverse=True, key=lambda x: x[1])

sum =0
for i in range(1,n+1):
    if deadline[i:]:
        for b in deadline[i:]:
            if b:
                big = b.pop(0)
                sum += big[1]
                break
    else:
        break
print(sum)

# import sys, heapq
# import time

# input = sys.stdin.readline

# n = int(input())

# problems = [list(map(int, input().split())) for _ in range(n)]

# start = time.time()
# problems.sort()
# queue = []
# for deadline, cupRamen in problems:
#     heapq.heappush(queue, cupRamen)
#     if deadline < len(queue):
#         heapq.heappop(queue)

# print(sum(queue))
# end = time.time()
# print(f"time : {end-start}")