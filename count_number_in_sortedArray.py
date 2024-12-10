from bisect import bisect_left, bisect_right

def count_bisect(array, left_num, right_num):
    right_index = bisect_right(array, right_num)
    left_index = bisect_left(array, left_num)
    result = right_index - left_index

    return result if result else -1

n,x = map(int,input().split())  
map =list(map(int,input().split())) 

result = count_bisect(map, x,x)
print(result)