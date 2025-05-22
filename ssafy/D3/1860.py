def solve(people, make_time, bread, come_time):
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
        total_bread[time]


T = int(input())
for t in range(1, T + 1):
    people, make_time, bread = map(int, input().split())
    come_time = list(map(int, input()))
