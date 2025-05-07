char = input().strip()
alpha = [0]*26
for i in char:
    alpha[ord(i.upper())-ord('A')] += 1
max_value = max(alpha)
result = []
for i in range(26):
    if len(result) >=2:
        break
    if alpha[i] == max_value:
        result.append(chr(ord('A')+i))
print(result[0] if len(result) == 1 else '?')