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
#  바꿔야 하는 갯수
cnt = 0
idx += 1
while idx < len(order_item):
    if order_item[idx] in used:
        idx += 1
        continue
    else:
        if idx + n <= len(order_item):
            next_item = set(order_item[idx : idx + n])
            delete_item = used - next_item
            used = next_item
            cnt += len(delete_item)
            idx += n
        else:
            next_item = set(order_item[idx:])
            update_item = next_item - used
            cnt += len(update_item)
            break

print(cnt)
