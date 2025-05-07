char = input().strip()
alpha = [-1] *26

for i in range(len(char)):
    index = ord(char[i]) - ord('a')
    if alpha[index] == -1:
        alpha[index] = i
print(*alpha)