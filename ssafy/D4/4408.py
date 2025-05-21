# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    goal = []
    for n in range(N):
        start, end = map(int, input().split())
        goal.append([min(start, end), max(start, end)])
    load = [False] * 201
    for start, end in goal:
        s = (start + 1) // 2
        e = (end + 1) // 2
        for i in range(s, e + 1):
            load[i] += 1
    print(f"#{t} {max(load)}")
