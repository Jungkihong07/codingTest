def average(_list: list):
    return round(sum(_list) / len(_list))


def solve(_list: list):
    _max = max(_list)
    _min = min(_list)
    _list.remove(_min)
    _list.remove(_max)
    return average(_list)


T = int(input())
for i in range(1, T + 1):
    _list = list(map(int, input().split()))
    print(f"#{i} {solve(_list)}")
