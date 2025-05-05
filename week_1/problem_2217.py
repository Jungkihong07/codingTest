import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

def is_can(ropes:list):
    max = 0
    ropes.sort(reverse=True)
    for i in range(n):
        max_weight= ropes[i]*(i+1) # 최고 무게 설정 = 선택한 선 중 최소 중량 * 선의 갯수
        if max_weight > max:
            max = max_weight
    return max

result = is_can(rope)
print(result)