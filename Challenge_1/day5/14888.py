from itertools import permutations
import math


def calculate(f_list: list, n_list: list[int]):
    sum = n_list[0]
    for i in range(len(f_list)):
        if f_list[i] == "+":
            sum += n_list[i + 1]
        elif f_list[i] == "-":
            sum -= n_list[i + 1]
        elif f_list[i] == "/":
            temp = sum / n_list[i + 1]
            sum = math.ceil(temp) if temp < 0 else int(temp)
        elif f_list[i] == "*":
            sum *= n_list[i + 1]
    return sum


n = int(input())
n_list = list(map(int, input().split()))

f_list = list(map(int, input().split()))

f = []
for i in range(4):
    if i == 0:
        c = "+"
    elif i == 1:
        c = "-"
    elif i == 2:
        c = "*"
    elif i == 3:
        c = "/"
    for _ in range(f_list[i]):
        f.append(c)

min = None
max = None

for l in permutations(f, len(f)):
    num = calculate(l, n_list)
    if (min == None) or (min > num):
        min = num
    if (max == None) or (max < num):
        max = num
print(max)
print(min)
