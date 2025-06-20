# 해당 방식은 stack을 활용해서 푼 문제임. 이에 대해 아무래도 GPT 참고해서 푼거다보니까. 아쉬움.
# 시간 복잡도는 O(n)임. stack에 걸쳐서 계산하는 것 뿐이니까. 시간 효율성에서 아쉽지는 않긴 한데, 해당 아이디어를 떠올리는데 시간이 걸릴 거 같음.

s_list = list(input().strip())


def solve(s_list):
    q = []
    for c in s_list:
        if c in ["(", "["]:
            q.append(c)
        else:
            temp = 0
            while q:
                top = q.pop()
                if isinstance(top, int):
                    temp += top
                elif c == "]" and top == "[":
                    q.append(3 if temp == 0 else temp * 3)
                    break
                elif c == ")" and top == "(":
                    q.append(2 if temp == 0 else temp * 2)
                    break
                else:
                    return 0
            else:
                return 0
    result = 0
    for item in q:
        if isinstance(item, str):
            return 0
        else:
            result += item
    return result


print(solve(s_list))
