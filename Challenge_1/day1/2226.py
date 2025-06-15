n = int(input())

prev = 0
current = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        current = prev * 2 + 1
    else:
        current = prev * 2 - 1
    prev = current
print(current if n != 1 else 0)
