array = [7,5,9,0,3,1,6,2]

for i in range(len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)