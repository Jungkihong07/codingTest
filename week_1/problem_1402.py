t = int(input())
a,b = map(int,input().split())

def find_divisors(n):
    result = []
    for i in range(1,n):
        if n % i == 0:
            result.append(i)
    return result

def solve(a:int,b:int):
    divisor = []
    for i in range(1,a+1):
        if a%i == 0:
            i_factor = find_divisors(i)
            for a in range(i_factor):
                _sum = sum()
            
