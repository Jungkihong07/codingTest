import sys
from decimal import Decimal
x,y = map(int,input().split())
z = int(Decimal(y)/Decimal(x)*100)
end = sys.maxsize
start = 1
result = 0
while(start <= end):
    total = 0
    mid = (end+start) //2 or 1
    total = int(Decimal(y+mid)/Decimal(x+mid)*100) 
    if total > z:
        result = mid
        end = mid -1
    else:
        start = mid + 1

print(result or -1)