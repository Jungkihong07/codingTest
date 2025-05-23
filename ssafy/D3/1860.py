import sys

sys.stdin = open('input.txt', 'r')


def solve(make_time, bread, come_time):
    current_bread = 0
    come_time.sort()
    cnt = 0
    for time in range(come_time[-1] + 1):
        if time % make_time == 0 and time != 0:
            current_bread += bread
        while cnt < len(come_time) and come_time[cnt] == time:
            current_bread -= 1
            cnt += 1
            if current_bread < 0:
                return False
    return True


T = int(input())
for t in range(1, T + 1):
    n, m, k = map(int, input().split())
    come_time = list(map(int, input().split()))
    result = "Possible" if solve(make_time=m, bread=k, come_time=come_time) else "Impossible"
    print(f"#{t} {result}")
