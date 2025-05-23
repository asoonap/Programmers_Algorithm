
# [PCCE 기출문제] 5번 / 심폐소생술
cpr1 = ["call", "respiration", "repeat", "check", "pressure"]	
answer1 = [2, 4, 5, 1, 3]
cpr2 = ["respiration", "repeat", "check", "pressure", "call"]	
answer2 = [4, 5, 1, 3, 2]


def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer


print(solution(cpr1))
print(solution(cpr2))