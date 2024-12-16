T = int(input())
array = [[0,0,0] for _ in range(41)]
array[0] = [1,0,0]
array[1] = [0,1,1]

def fibonacci(n):
    if n == 0:
        return array[n][2]
    elif n == 1:
        return array[n][2]
    if array[n][2]:
        return array[n][2]
    array[n][2] = fibonacci(n-1) + fibonacci(n-2)
    array[n][0] = array[n-1][0] + array[n-2][0]
    array[n][1] = array[n-1][1] + array[n-2][1]
    return array[n][2]

result = []
for _ in range(T):
    n = int(input())
    fibonacci(n)
    result.append([array[n][0],array[n][1]])

for a, b in result:
    print(a,b)