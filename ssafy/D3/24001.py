def solve(code: list):
    max_index = 0
    for prompt in ["L", "R"]:
        _index = []
        index = 0
        for c in code:
            if c == "?":
                c = prompt
            if c == "L":
                index -= 1
                _index.append(abs(index))
            elif c == "R":
                index += 1
                _index.append(abs(index))
        max_index = max(max(_index), max_index)
    return max_index


T = int(input())
for i in range(1, T + 1):
    code = list(map(str, input().strip()))
    print(solve(code))
