from bisect import bisect_left, bisect_right

# 해당 문제는 백준 1920번 문제입니다.

n = int(input())
list_n = list(map(int,input().split())) 
m = int(input())    
list_m = list(map(int,input().split()))
list_n.sort()
def bisect_count(a, left_num, right_num):
    right_index = bisect_right(a, right_num)
    left_index = bisect_left(a, left_num)
    return right_index-left_index

for i in list_m:
    result = bisect_count(list_n, i,i)
    print(1 if result else 0)