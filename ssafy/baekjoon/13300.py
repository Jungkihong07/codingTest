import math

n, k = map(int, input().split())
f_room = [0] * 7
m_room = [0] * 7
for i in range(n):
    s, y = map(int, input().split())
    if s == 1:
        m_room[y] += 1
    else:
        f_room[y] += 1
result = 0
for grade in range(1, 7):
    result += (m_room[grade] + k - 1) // k + (f_room[grade] + k - 1) // k
print(result)
