left, right = map(int, input().split())

sum_list = [0]
sum = 0
for num in range(1, right + 1):
    for i in range(num):
        sum += num
        sum_list.append(sum)
print(sum_list[right] - sum_list[left - 1])
