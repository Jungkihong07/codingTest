n = int(input())
list_n = list(map(int, input().split()))
list_n.sort()

result = 0
count = 0

for i in list_n:
  count += 1  #현재 그룹에 하나씩 포함하기
  if count >= i:  #현재 그룹에 포함된 모험가의 수가 현재의 콩포도 이상이라면, 그룹 결성
    result += 1  #결성한 그룹 수 증가
    count = 0  # 포함한 모험사의 수 초기화

print(result)

