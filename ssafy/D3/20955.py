# 이거 틀렸음 다시 풀자.

import sys

sys.stdin = open("input.txt", "r")


def fun_1(s: str):
    return s + "X"


def fun_2(s: str):
    return s[::-1] + "Y"


def is_true(s, e):
    from collections import deque

    queue = deque([s])
    visited = set([s])  # 중복 제거를 위해 방문 추적

    while queue:
        curr = queue.popleft()
        if curr == e:
            return True
        if len(curr) >= len(e):
            continue
        for next_str in [fun_1(curr), fun_2(curr)]:
            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)
    return False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    e = input()
    print("Yes" if is_true(s, e) else "No")
