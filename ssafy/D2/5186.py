# 문제 해결 완료
T = int(input())


def solve(n: float):
    _list = []
    digit = 0.5
    while n > 0 and len(_list) <= 12:
        if n >= digit:
            n -= digit
            _list.append(1)
        else:
            _list.append(0)
        digit *= 0.5
    return "".join(map(str, _list)) if len(_list) <= 12 else "overflow"


for i in range(1, T + 1):
    n = float(input())
    print(f"#{i} {solve(n)}")
