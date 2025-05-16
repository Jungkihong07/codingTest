def operate(hill_num, d):
    rotate_list = [0] * 5  # 1~4번 톱니바퀴의 회전 방향 기록용 (0: 회전 안 함)
    rotate_list[hill_num] = d

    # 오른쪽 확인 (hill_num → 4)
    for i in range(hill_num, 4):
        if hill[i][2] != hill[i + 1][6]:
            rotate_list[i + 1] = -rotate_list[i]
        else:
            break

    # 왼쪽 확인 (hill_num → 1)
    for i in range(hill_num, 1, -1):
        if hill[i][6] != hill[i - 1][2]:
            rotate_list[i - 1] = -rotate_list[i]
        else:
            break

    # 회전 적용
    for i in range(1, 5):
        if rotate_list[i] != 0:
            hill[i] = move(rotate_list[i], hill[i])


def move(d, hill: list):
    return hill[1:] + [hill[0]] if d == -1 else [hill[-1]] + hill[:-1]


hill = [[0]]
for _ in range(4):
    hill.append(list(map(int, input().strip())))
k = int(input())
for _ in range(k):
    hill_num, d = map(int, input().split())
    operate(hill_num, d)

total = 0
for i in range(1, 5):
    if i == 1:
        total += 1 if hill[i][0] else 0
    elif i == 2:
        total += 2 if hill[i][0] else 0
    elif i == 3:
        total += 4 if hill[i][0] else 0
    elif i == 4:
        total += 8 if hill[i][0] else 0
print(total)
