def solve(make_time, bread, come_time):
    current_bread = 0
    total_time = sum(come_time)
    total_bread = []
    for i in range(total_time):
        if i % make_time == 0:
            current_bread += bread
        total_bread.append(current_bread)
    time = 0
    for i in come_time:
        time += i
        for j in range(time, total_time):
            total_bread[j] -= 1
            if total_bread[j] < 0:
                return False
    return True


T = int(input())
for t in range(1, T + 1):
    people, make_time, bread = map(int, input().split())
    come_time = list(map(int, input()))
    print(f"#{t} {solve(make_time, bread, come_time)}")
