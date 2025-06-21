# 해당 아이디어를 떠올리는 데 시간이 조금 걸리는 거롤 보아.. 아직 나는 실력이 많이 부족한가보다.. ㅠ. 아니 솔직히 말해서 떠올렸다고 하기에도 그렇지..  ㅠ

h, w = map(int, input().split())
board = list(map(int, input().split()))

result = 0
for idx in range(1, w - 1):
    left_max = max(board[:idx])
    right_max = max(board[idx + 1 :])
    h = min(left_max, right_max)
    if h > board[idx]:
        result += h - board[idx]
print(result)
