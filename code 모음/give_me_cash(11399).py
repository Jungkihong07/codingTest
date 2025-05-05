time = int(input())
people = list(map(int, input().split()))
people.sort()
result =0
waiting_time=0
for i in people:
  waiting_time += i
  result += waiting_time

print(result)