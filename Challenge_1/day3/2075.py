import heapq

n = int(input())
heap = []

for _ in range(n):
    row = list(map(int, input().split()))
    for num in row:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
print(heap[0])
