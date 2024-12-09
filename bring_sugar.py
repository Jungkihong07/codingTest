n = int(input())
large = 5
small = 3
count = 0
while True:
  if (n % large == 0):
    count += n // large
    n = n % large
    break
  else:
    n -= small
    count += 1
    if (n <= 0):
      break
if (n == 0):
  print(count)
else:
  print(-1)
