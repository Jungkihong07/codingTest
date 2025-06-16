people = 0
max_num = 0
for i in range(10):
    a, b = map(int, input().split())
    people = people - a + b
    max_num = max(max_num, people)
print(max_num)
