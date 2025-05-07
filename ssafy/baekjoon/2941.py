# 주의할 점. 조건문에 의존해서 적지 말 것.
char = input().strip()
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
cnt = 0
while i < len(char):
    if char[i:i+3] == "dz=":  # 가장 긴 조합 먼저 확인
        i += 3
    elif char[i:i+2] in croatian:
        i += 2
    else:
        i += 1
    cnt += 1

print(cnt)