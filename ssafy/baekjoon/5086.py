def solve(a: int, b: int):
    if a % b == 0:
        return 'multiple'
    elif b % a == 0:
        return 'factor'
    else:
        return 'neither'


while 1:
    try:
        a, b = map(int, input().split())
        print(solve(a, b))
    except EOFError:
        exit(0)
    except ZeroDivisionError:
        exit(0)
