t = int(input())
is_mod = [0] * 1001
for i in range(2, 1001):
    if not is_mod[i]:
        is_mod[i] = 1
        num = i
        while 1:
            num += i
            if num > 1000:
                break
            is_mod[num] = 2

_result = list(map(int, input().split()))
cnt = 0
for i in _result:
    if is_mod[i] == 1:
        cnt += 1
print(cnt)
