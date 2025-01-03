import heapq

# 오름차순 정렬
def heapsort(iterable):
    h =[]
    result =[]
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,5,6,8,9])
print(result)