data = input()
# 첫 번째 문자를 숫자로 바꾸어 대입
result = int(data[0])
for a in data[1:]:
  num = int(a)
  # 둘 중에 하나라도 0 혹은 1인 경우, 곱하기 보다는 더하기 수행
  if result <= 1 or num <=1:
    result += num
  else:
    result *= num
print(result)