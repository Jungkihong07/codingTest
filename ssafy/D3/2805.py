import sys

sys.stdin = open('input.txt', 'r')

import math


def solve(farm, n):
    mid = math.ceil(n // 2)
    result = 0
    end = mid
    for row in range(n):
        if row <= mid:
            end += 1
        else:
            end -= 1
        for col in range(abs(mid - row), end):
            result += farm[row][col]
    return result


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    farm = [list(map(int, input().strip())) for _ in range(n)]
    print(f"#{t} {solve(farm, n)}")
