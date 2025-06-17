n = int(input())
nums = list(map(int, input().split()))
decimal_list = [0, 0] + [1] * 1000

for i in range(2, 101):
    if decimal_list[i] == 1:
        index = i + i
        while index < len(decimal_list):
            decimal_list[index] = 0
            index += i

result = 0
for num in nums:
    result += decimal_list[num]
print(result)
