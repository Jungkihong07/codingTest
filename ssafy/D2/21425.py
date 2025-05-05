# 해결 완료.
T = int(input())


def solve(a, b, n):
    cnt = 0
    while a <= n and b <= n:
        if a >= b:
            b += a
        elif b > a:
            a += b
        cnt += 1
    return cnt


for i in range(1, T + 1):
    a, b, n = map(int, input().split())
    print(solve(a, b, n))
