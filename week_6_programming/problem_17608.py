import sys

input = sys.stdin.readline
n = int(input())
list_n = []
for _ in range(n):
    list_n.append(int(input()))

list_n.reverse()


def count_num(list_n):
    min = 0
    count = 0
    for i in list_n:
        if min < i:
            min = i
            count += 1
    return count


print(count_num(list_n))
