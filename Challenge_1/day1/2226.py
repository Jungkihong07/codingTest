import sys

input = sys.stdin.readline

n = int(input())

bisect = [[1001]]

ch = 1

for i in range(2, n):
    reverse_temp = []
    for ch in bisect:
        if ch == [1001]:
            reverse_temp.append([0110])
        else:
            reverse_temp.append([1001])
    bisect = reverse_temp + bisect
    print(*bisect)
