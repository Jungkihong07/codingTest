# dfs 구현 version . 이해하는 데 시간이 조금 걸리고, 생각보다 조건이 많이 있어. 구현하기 힘들어보인다. 조금 더 연습해야 할까.?


s_list = list(input().strip())


def dfs(index):
    result = 0
    while index < len(s_list):
        # Case 1
        if s_list[index] in ["(", "["]:
            # 다음 index 조회
            temp, next_index = dfs(index + 1)
            # 만약 아무것도 없다면, 그건 o
            if not temp:
                return 0, len(s_list)
            # index가 넘어갔다면, 0
            if next_index >= len(s_list):
                return 0, len(s_list)
            # 원하는 조건에 부합한다면, result 업데이트
            if s_list[index] == "(" and s_list[next_index] == ")":
                result += 2 * temp
            elif s_list[index] == "[" and s_list[next_index] == "]":
                result += 3 * temp
            # 어느 조건에도 부합하지 않는다면, 0
            else:
                return 0, len(s_list)
            index = next_index + 1
        # Case 2
        elif s_list[index] in [")", "]"]:
            return (1 if result == 0 else result), index
        else:
            return 0, len(s)
    return result, index


result, last_index = dfs(0)
print(result if last_index == len(s_list) else 0)
