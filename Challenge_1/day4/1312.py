a, b, c = map(int, input().split())

a = a * (10**c)
result = a // b
result = str(result)
print(result[-1])
