# 코드 개선 점 많음. 다시 리팩토링 해보기

n, k = map(int, input().split())

order_item = list(map(int, input().split()))

# 현재 사용하고 있는 콘셉트
used: set = set()
idx = 0
# 현재 사용할 콘셉트와 순서 저장
for i in range(len(order_item)):
    if len(used) < n:
        used.add(order_item[i])
        idx = i
    else:
        break
#  바꿔야 하는 갯수
cnt = 0
idx += 1
while idx < len(order_item):
    if order_item[idx] in used:
        idx += 1
        continue
    else:
        remove_item = set()
        i = 0
        while not remove_item and k - i >= idx:
            next_item = set(order_item[idx : k - i])
            remove_item = used - next_item
            i += 1
        used.remove(remove_item.pop())
        cnt += 1
        used.add(order_item[idx])
        idx += 1

print(cnt)
