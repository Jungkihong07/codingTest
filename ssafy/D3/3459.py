# 문제 해결 못함. 나중에 풀어보기

import sys

sys.stdin = open("sample_input.txt", 'r')

t = int(input())
for test_case in range(1, t + 1):
    N = int(input())
    while N > 3:
        N = N // 2 + 1  # 공격자가 부르고 싶은 수
        N = N // 2 - 1  # 공격자가 부르고 싶은 수를 못부르게 막는 방어자의 수

    result = ''
    if N >= 2 or N == 0:  # 공격자가 2,3의 수를 시작으로 자신이 원하는 수를 만들 수 있다면 Alice 승
        result = 'Alice'

    else:
        result = 'Bob'

    print(f'#{test_case} {result}')
