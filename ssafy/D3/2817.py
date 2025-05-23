import sys

sys.stdin = open('sample_input.txt', 'r')
#
# from collections import deque
#
#
# def solve(index, c_sum):
#     if c_sum == k:
#         return 1
#     if index == n:
#         return 0
#
#     pick = solve(index + 1, c_sum + n_list[index])
#     no_pick = solve(index + 1, c_sum)
#
#     return no_pick + pick
#
#
from itertools import combinations


def solve(n, k, n_list):
    num = 0
    for i in range(1, n + 1):
        for comb in combinations(n_list, i):
            if sum(comb) == k:
                num += 1
    return num


T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    n_list = list(map(int, input().split()))
    print(f"#{t} {solve(n, k, n_list)}")
    # print(f"#{t} {solve(0, 0)}")
