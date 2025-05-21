import sys

sys.stdin = open('sample_input.txt', 'r')


def solve(item, max_cal):
    cal_list = [0] * (max_cal + 1)
    for score, cal in item:
        for i in range(max_cal, cal - 1, -1):
            cal_list[i] = max(cal_list[i], cal_list[i - cal] + score)
    return max(cal_list)


T = int(input())

for t in range(1, T + 1):
    n, max_cal = map(int, input().split())
    item = [tuple(map(int, input().split())) for _ in range(n)]
    print(f"#{t} {solve(item, max_cal)}")
