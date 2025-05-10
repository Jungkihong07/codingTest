h, m = map(int, input().split())


def calculate(h, m):
    m -= 45
    at = abs(m) // 60 + 1 if m < 0 else 0
    m = m % 60
    h -= at
    h %= 24

    return h, m


h, m = calculate(h, m)
print(h, m)
