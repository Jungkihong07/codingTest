n,k = map(int,input().split())

list_n = [int(input()) for _ in range(n)]

def solve_problem(array, start, end):
    while start<=end:
        mid = (end+start)//2 or 1
        total = 0
        for lan in array:
            if lan>=mid:
                total += lan // mid
        if total < k:
            end = mid -1
        else:
            result = mid
            start = mid + 1
    return result

end = max(list_n)
result = solve_problem(list_n,0,end)
print(result)