n, s = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()


min = 1000000000
sum_list = n_list
for i in range(2, n + 1):
    compare_list = []
    for j in range(n):
        max_item = max(sum_list[j - i : j + 1])
        compare_list.append()
