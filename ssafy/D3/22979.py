def operate(s: list, x_list: list):
    for x in x_list:
        x %= len(s)
        if x > 0:
            for _ in range(x):
                s = s[1:] + s[0]
        elif x < 0:
            for _ in range(abs(x)):
                s = s[-1] + s[:-1]
        else:
            pass
    return s


T = int(input())
for i in range(1, T + 1):
    s = input().strip()
    k = int(input())
    _list = list(map(int, input().split()))
    print(operate(s, _list))
