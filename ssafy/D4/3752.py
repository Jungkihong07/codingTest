# 해당 문제는 테크닉이 필요한 문제로 보여진다. 다음부터는 이러한 식으로 하면 된다는 것을 숙지하자.
def solve(_list: list):
    result = set([0])
    for score in _list:
        for i in range(10000, -1, -1):
            if i in result:
                result.add(i + score)
    return len(result)


T = int(input())
for i in range(1, T + 1):
    n = int(input())
    _list = list(map(int, input().split()))
    print(f"#{i} {solve(_list)}")
