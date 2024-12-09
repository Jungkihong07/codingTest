n_k = list(map(int, input().split()))
coin_list = []
for i in range(n_k[0]):
  coin = int(input())
  coin_list.append(coin)

coin_list.reverse()

count = 0
for coin in coin_list:
  if coin <= n_k[1]:
    count += n_k[1] // coin
    n_k[1] = n_k[1] % coin

print(count)
