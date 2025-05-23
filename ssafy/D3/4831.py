import sys

sys.stdin = open('sample_input.txt', 'r')


def solve(end, k, charged_places):
    min_value = 0
    current = 0
    while current + k < end:
        for r in range(k, 0, -1):
            if (current + r) in charged_places:
                current += r
                min_value += 1
                break
        else:
            return 0
    return min_value


# def solve(end, k, charged_places):
#     current = 0
#     charge_count = 0
#     charged_set = set(charged_places)
#
#     while current + k < end:
#         # 가장 멀리 있는 충전소 찾기
#         for step in range(k, 0, -1):
#             if (current + step) in charged_set:
#                 current += step
#                 charge_count += 1
#                 break
#         else:
#             return 0  # 이동 가능한 충전소 없음
#     return charge_count


T = int(input())
for t in range(1, T + 1):
    k, end, charged_num = map(int, input().split())
    charged_places = list(map(int, input().split()))
    min_value = solve(end, k, charged_places)
    print(f"#{t} {min_value if min_value != 999 else 0}")
