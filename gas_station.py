station = int(input())

gas = list(map(int, input().split()))

cost = list(map(int, input().split()))

min_cost = min(cost[:station - 1])
result = 0
for i in range(station - 1):
  recent = cost[i]
  if (recent > min_cost):
    result += gas[i] * recent
  else:
    result += recent * sum(gas[i:])
    break

print(result)
