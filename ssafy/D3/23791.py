def set_index(s: list, index, index_list: list, c: str):
    while (len(index_list) - 1) > index:
        if s[index_list[index] - 1] == "":
            return index
        else:
            index += 1
    return index


def solve(n: int, a: list, b: list):
    remain = n
    a_index = 0
    b_index = 0
    s = ["" for _ in range(n)]
    while remain > 0:
        a_index = set_index(s, a_index, a, "A")
        s[a[a_index] - 1] = "A"
        remain -= 1
        if remain <= 0:
            break
        b_index = set_index(s, b_index, b, "B")
        s[b[b_index] - 1] = "B"
        remain -= 1
    return "".join(s)


T = int(input())
for i in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
