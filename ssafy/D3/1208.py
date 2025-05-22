import sys

sys.stdin = open("/workspaces/codingTest/ssafy/D3/input.txt", "r")

for t in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))
    while n:
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
        n -= 1
    result = max(boxes) - min(boxes)
    print(f"#{t} {result}")
