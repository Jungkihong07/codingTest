import sys

input = sys.stdin.readline

n, k = map(int, input().split())

_list = [i for i in range(1, n + 1) if n % i == 0]

print(_list[k - 1] if len(_list) >= k else 0)
