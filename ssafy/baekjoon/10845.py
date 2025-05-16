from collections import deque
import sys

input = sys.stdin.readline


def operate(c: str, num: int = None):
    if c == 'push':
        q.append(num)
        return None
    elif c == 'pop':
        return q.popleft() if q else -1
    elif c == 'size':
        return len(q)
    elif c == 'empty':
        return 0 if q else 1
    elif c == 'front':
        return q[0] if q else -1
    elif c == 'back':
        return q[-1] if q else -1
    else:
        return None


t = int(input())
q = deque()
for _ in range(t):
    input_list = list(map(str, input().split()))
    c = input_list[0]
    num = int(input_list[1]) if len(input_list) >= 2 else None
    result = operate(c, num)
    if result is not None:
        print(result)
