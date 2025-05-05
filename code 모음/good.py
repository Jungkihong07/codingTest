# 백준의 1253번 문제이다.

n = int(input())
m = list(map(int,input().split()))

def is_good(num):
    ex_m = m[0:num] + m[num+1:]
    start = 0
    end = len(ex_m)-1
    while start < end:
        total = ex_m[start] + ex_m[end]
        if total == m[num]:
            return True
        elif total < m[num]:
            start+=1
        else:
            end -=1
    return False

m.sort()

result = 0
for i in range(n):
    result += 1 if is_good(i) else 0
print(result)