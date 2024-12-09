import time
# 1이 될 때까지
N = int(input())
K = int(input())
start = time.time()
count = 0
while N != 1:
  if N % K == 0:
    N = N // K
    count += 1
  else:
    N -= 1
    count += 1
print(count)
end = time.time()
print(f"time = {end-start}")
