n,k = map(int,input().split())

list_n = [int(input()) for _ in range(n)]

def solve_problem(array, start, end):
    while start<=end:
        total = 0
        for lan in array:
            if lan >= end:
                total += lan // end
        if total < k:
            end = (start + end) //2
        else:
            return end

end = max(list_n)
result = solve_problem(list_n,0,end)
print(result)