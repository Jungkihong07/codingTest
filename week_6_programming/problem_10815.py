# [백준] 10815번 숫자 카드
import sys


input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
m = int(input())

is_list = list(map(int, input().split()))


sorted_list = sorted(list_n)


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


result = []
for y in is_list:
    result.append(1 if binary_search(sorted_list, y, 0, len(sorted_list) - 1) else 0)

print(*result)
