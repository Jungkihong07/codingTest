# 정렬되어 있는 리스트에 한해서 사용 가능.
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start= mid +1
    return None

# n(원소의 개수)가 target(찾고자 하는 값)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행결과 출력
result = binary_search(array, target, 0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)