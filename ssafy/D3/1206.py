import sys

sys.stdin = open('sample_input.txt', 'r')
for t in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    max_h = max(height)
    buildings = [[0] * n for _ in range(max_h)]
    total = 0
    for i in range(n):
        for h in range(height[i]):
            buildings[h][i] = True
    for i in range(n):
        for h in range(height[i]):
            is_good = True
            for col in [-2, -1, 1, 2]:
                if buildings[h][i + col]:
                    is_good = False
                    break
            if is_good:
                total += 1
    print(f"#{t} {total}")
