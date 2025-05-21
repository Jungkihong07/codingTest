## 해당 문제 다시 풀기


import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

T = int(input())


def solve(n_list, b):
    w = len(n_list)
    q = deque()
    visited = set()
    q.append([tuple(n_list), 0])
    max_value = 0
    while q:
        c_list, cnt = q.popleft()
        c_list = list(c_list)
        if cnt == b:
            max_value = max(max_value, int(''.join(map(str, c_list))))
            continue
        for i in range(w):
            for j in range(i + 1, w):
                temp = c_list[:]
                temp[i], temp[j] = temp[j], temp[i]
                temp = tuple(temp)
                if (temp, cnt + 1) not in visited:
                    visited.add((temp, cnt + 1))
                    q.append([temp, cnt + 1])
    return max_value


for t in range(1, T + 1):
    a, b = input().split()
    n_list = [int(i) for i in a]
    b = int(b)
    print(f"#{t} {solve(n_list, b)}")

# def solve(n_list, b):
#     w = len(n_list)
#     q = deque()
#     q.append((n_list, 0))
#     visited = set()
#     max_result = 0
#
#     while q:
#         c_list, cnt = q.popleft()
#         c_tuple = tuple(c_list)
#         if (c_tuple, cnt) in visited:
#             continue
#         visited.add((c_tuple, cnt))
#
#         if cnt == b:
#             max_result = max(max_result, int(''.join(map(str, c_list))))
#             continue
#
#         for i in range(w):
#             for j in range(i + 1, w):  # i == j인 경우는 swap 의미 없음
#                 new_list = c_list[:]
#                 new_list[i], new_list[j] = new_list[j], new_list[i]
#                 q.append((new_list, cnt + 1))
#
#     return [int(x) for x in str(max_result)]
#
#
# for t in range(1, T + 1):
#     a, b = input().split()
#     a_list = [int(i) for i in a]
#     b = int(b)
#     a_list = solve(a_list, b)
#     print(f"#{t} ", end='')
#     for i in a_list:
#         print(i, end='')
#     print()
