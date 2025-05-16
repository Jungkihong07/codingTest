n = int(input())
stack = []
out_list = []
pl = []
stack_top = 1
possible = True
for i in range(n):
    num = int(input())
    if stack_top <= num:
        for item in range(stack_top, num + 1):
            stack.append(item)
            pl.append('+')
        stack_top = num + 1
    if stack[-1] == num:
        out_list.append(stack.pop())
        pl.append('-')
    else:
        possible = False
        break
if possible:
    for p in pl:
        print(p)
else:
    print("NO")
