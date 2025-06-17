a, b = map(int, input().split())

minNum = min(a, b)
for i in range(minNum, -1, -1):
    if a % i == 0 and b % i == 0:
        first = i
        second = i * (a // i) * (b // i)
        break
print(first)
print(second)
