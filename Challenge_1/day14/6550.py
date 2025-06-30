while 1:
    try:
        s, t = input().split()
        search_len = len(s)
        stack = []
        for item in s:
            for idx in range(len(t)):
                if item == t[idx]:
                    stack.append(item)
                    t = t[idx + 1 :]
                    break
            if item not in stack:
                break
        print("Yes" if "".join(stack) == s else "No")
    except EOFError:
        break
    except ValueError:
        break
