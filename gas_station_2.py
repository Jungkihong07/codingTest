station = int(input())

gas = list(map(int, input().split()))

cost = list(map(int, input().split()))

result = 0

pay = cost[0]

for i in range(station-1):
  if(cost[i] > pay):
    result += gas[i] * pay
  else:
    pay = cost[i]
    result += gas[i] * pay

print(result)
