from collections import deque
import sys

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

q = deque()

min_len = sys.maxsize
sum_n = 0

for item in n_list:
    q.append(item)
    sum_n += item
    while s <= sum_n:
        min_len = min(min_len, len(q))
        sum_n -= q.popleft()

print(min_len if min_len < sys.maxsize else 0)
