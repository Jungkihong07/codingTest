def solve(a, b):
    # max_val = max(a, b)
    # num = 0
    # for i in range(max_val, 0, -1):
    #     if a >= i and b >= i:
    #         if a % i == 0 and b % i == 0:
    #             num = i
    #             break
    # a = a // num
    # b = b // num
    # return a * b * num
    return a * b // gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))
