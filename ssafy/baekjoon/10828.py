from collections import deque
import sys

input = sys.stdin.readline


def process(cmd, num=None):
    if cmd == 'push':
        stack.append(num)
        return None
    elif cmd == 'pop':
        if stack:
            return stack.pop()
        else:
            return -1
    elif cmd == 'size':
        return len(stack)
    elif cmd == 'empty':
        if stack:
            return 0
        else:
            return 1
    elif cmd == 'top':
        if stack:
            return stack[-1]
        else:
            return -1


t = int(input())
stack = deque()
for _ in range(t):
    ele = list(map(str, input().split()))
    if len(ele) >= 2:
        element = process(ele[0], int(ele[1]))
    else:
        element = process(ele[0])
    if None != element:
        print(element)
    else:
        continue
