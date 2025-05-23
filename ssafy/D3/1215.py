import sys

sys.stdin = open('input.txt', 'r')
for t in range(1, 11):
    n = int(input())
    board = [list(map(str, input().strip())) for _ in range(8)]
    dx = [0, n]
    dy = [n, 0]
    cnt = 0
    for row in range(8):
        for col in range(8):
            for d in range(2):
                nx = col + dx[d]
                ny = row + dy[d]
                if 0 <= nx <= 8 and 0 <= ny <= 8:
                    if d == 0:
                        new_list = []
                        idx = row
                        while idx != ny:
                            new_list += board[idx][col]
                            idx += 1
                        if new_list == new_list[::-1]:
                            cnt += 1
                    elif d == 1:
                        new_list = board[row][col:nx]
                        if new_list == new_list[::-1]:
                            cnt += 1
    print(f"#{t} {cnt}")
