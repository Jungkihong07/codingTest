n = int(input())
nums = list(map(int, input().split()))
MAX = max(nums) + 1
decimal_list = [0, 0] + [1] * MAX

for i in range(2, int(MAX**0.5) + 1):
    if decimal_list[i]:
        for j in range(i * i, MAX, i):
            decimal_list[j] = 0

result = 0
for num in nums:
    result += decimal_list[num]
print(result)
