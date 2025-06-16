from itertools import combinations

doll = [int(input()) for _ in range(9)]

for i in combinations(doll, 7):
    if sum(i) == 100:
        result = sorted(i)
        break

for i in result:
    print(i)
