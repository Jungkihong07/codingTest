a, b = map(int, input().split())
c = int(input())


def calculate(h, m, t):
    m = m + t
    ah = m // 60
    m %= 60
    h += ah
    h %= 24
    return h, m


hour, m = calculate(a, b, c)
print(f"{hour} {m}")
