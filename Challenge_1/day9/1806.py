# 해당 문제 유형을 풀어본 것이 처음이라, 시간이 오래 걸림. 해당 아이디어를 떠올리는데 시간이 오래 걸렸고, 잘 몰랐음.
import sys

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
start = 0
end = 0
min_len = sys.maxsize
sum_num = 0
while 1:
    if s <= sum_num:
        min_len = min(min_len, end - start)
        sum_num -= n_list[start]
        start += 1
    elif end == n:
        break
    else:
        sum_num += n_list[end]
        end += 1
print(min_len if min_len < sys.maxsize else 0)
