import sys
input= sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

def solve_problem(array, start, end):
    result = 0
    while(start <= end):
        mid = (start+end) //2 or 1
        total = 0
        for i in array:
            if i > mid:
                total += i - mid
        if total < m:
            end = mid -1
        else:
            result = mid
            start = mid +1
    return result


end=max(a)
print(solve_problem(a,1,end))