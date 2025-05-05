import sys
input= sys.stdin.readline

n = int(input())
m = list(map(int,input().split()))

def find_solutions(index):
    global result_list
    global result
    graph= m[index+1:]
    start = 0
    end = len(graph) -1
    while start < end:
        sample = (graph[start] + graph[end] + m[index])
        if abs(result) >= abs(sample):
            result_list = [m[index], graph[start] , graph[end]]
            result = sample
        if sample<0:
            start += 1
        elif sample>0:
            end -= 1
        else:
            break

m.sort()

result =3000000000
result_list= []

for i in range(len(m)):
    if result:
        find_solutions(i)
    else:
        break

print(f"{result_list[0]} {result_list[1]} {result_list[2]}") 