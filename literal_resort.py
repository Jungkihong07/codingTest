data = input()
result = []
value = 0

# 문자를 하나씩 확인하기
for a in data:
  # 만약 문자가 알파벳이라면
  if a.isalpha():
    result.append(a)
  else:
    value += int(a)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))
# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))
