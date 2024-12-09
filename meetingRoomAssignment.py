num = int(input())
meeting_room = []
# 미팅룸 접수하기
for i in range(num):
  meeting = list(map(int, input().split()))
  # 추가로 소요되는 시간 추가
  meeting.append(meeting[1] - meeting[0])
  meeting_room.append(meeting)
# 끝나는 시간, 시작하는 시간, 소요되는 시간 순으로 정렬
meeting_room.sort(key=lambda x: [x[1], x[0]])
# 가장 첫 번째 우선순위를 선택하여 진행
start = meeting_room[0]
count = 1
# 회의 시작하고, 입력된 회의만큼 반복하여 갯수 세기
for i in meeting_room[1:]:
  if i[0] >= start[1]:
    start = i
    count += 1
  else:
    continue

print(count)
