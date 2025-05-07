def solve(s: str, r: str):
    a = r
    while 1:
        if a == s:
            return "Yes"
        elif len(a) < len(s):
            return "No"
        if a[-1] == "X":
            a = a[:-1]
        elif a[-1] == "Y":
            a = a[:-1][::-1]


T = int(input())
for i in range(1, T + 1):
    s = input().strip()
    r = input().strip()
    print(f"#{i} {solve(s, r)}")
