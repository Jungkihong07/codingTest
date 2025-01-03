import sys
import copy

input = sys.stdin.readline
n, m = map(int, input().split())

a_name, b_name = map(str, input().split())

alphabet = [
    3,
    2,
    1,
    2,
    4,
    3,
    1,
    3,
    1,
    1,
    3,
    1,
    3,
    2,
    1,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    1,
    2,
    2,
    1,
]


size = min(n, m)

mix_str = ""

for i in range(size):
    mix_str += a_name[i] + b_name[i]
mix_str += a_name[size:] + b_name[size:]

result = []
for i in mix_str:
    index = ord(i) - 65
    result.append(alphabet[index])

while len(result) > 2:
    sum_result = []
    for i in range(len(result) - 1):
        item = (result[i] + result[i + 1]) % 10
        sum_result.append(item)
    result = copy.deepcopy(sum_result)

if not result[0]:
    print(f"{result[1]}%")
else:
    print(f"{result[0]}{result[1]}%")
