# 파이썬의 장점을 살린 방식
array = [7,5,9,0,3,1,6,2,4]

def quick_sort(array):
    # 만약 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    left_side = [x for x in tail if x <=pivot] # 분할된 왼쪽 부분
    right_side = [y for y in tail if y>pivot] # 분할된 오른족 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))