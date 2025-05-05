n = int(input())  
big = 5
small = 3
num =0
while True:
    if n % big == 0:
        num += n // big
        n %= big
        break
    else:
        n -= small
        num += 1
        if (n<0):
            break
if n == 0:
    print(num)
else:
    print(-1)