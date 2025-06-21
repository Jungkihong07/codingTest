# 생각할 수 있는 가장 일반적인 방법으로 풀이를 완료함. 집합을 계산한 가장 좋은 방법 중 하나로 보임. 또한 비트 연산자 방법도 있는데 그건 나중에 해보자.
from itertools import combinations


n, k = map(int, input().split())
essential = {"a", "n", "t", "i", "c"}
words: list[set] = []
need_char = set()

for _ in range(n):
    temp = list(input().strip())
    temp = set(temp[4:-4])
    words.append(temp)
    need_char.update(temp - essential)

if k < 5:
    print(0)
    exit()

if len(need_char) <= k - 5:
    print(len(words))
    exit()

max_result = 0
for comb in combinations(need_char, k - 5):
    search_char = essential.union(comb)
    num = 0
    for word in words:
        if word.issubset(search_char):
            num += 1
    max_result = max(max_result, num)
print(max_result)
