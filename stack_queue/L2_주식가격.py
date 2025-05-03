# 주식가격
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
# --------------------------------------------------

# 입출력 예
prices = [1, 2, 3, 2, 3]
# return = [4, 3, 1, 1, 0]

from collections import deque
def solution(prices):
    answer = []
    list = deque(prices)
    while list:
        target = list.popleft()
        time = 0
        for i in list:
            if target <= i:
                time += 1
        answer.append(time)
    return answer

print(solution(prices))

# --------------------------------------------------
# 시간 초과 문제
# 모든 원소에 대해 남아 있는 모든 원소를 다시 한 번 순회하기 때문에, 길이 N인 prices에 대해 대략 N + (N-1) + (N-2) + … + 1 = N(N+1)/2 만큼의 비교가 발생합니다.
# --------------------------------------------------

# gpt - 모노토닉 스택(monotonic stack) 풀이
prices = [1, 2, 3, 2, 3]
def solution2(prices):
    n = len(prices)
    answer = [0] * n
    stack = []          # 인덱스 저장용

    # 1) 순회하면서 “떨어짐 시점” 처리
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 2) 끝까지 떨어지지 않은 나머지 처리
    while stack:
        j = stack.pop()
        answer[j] = (n - 1) - j

    return answer

print(solution2(prices))


# --------------------------------------------------
# 추가 - 타입 힌트
# prices는 int 원소의 리스트이고, 함수도 int 리스트를 반환
from typing import List

def solution(prices: List[int]) -> List[int]:
    n = len(prices)
    answer = [0] * n
    stack: List[int] = []  # 인덱스를 저장할 스택

    for i, price in enumerate(prices):
        # 스택 탑에 저장된 인덱스의 가격이 현재 price보다 높으면
        # 그 인덱스의 '떨어지지 않은 기간'을 확정 짓고 꺼낸다.
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j

        # 현재 인덱스 i를 스택에 쌓아두고, 이후에 더 낮은 price가 오면 꺼낼 준비
        stack.append(i)

    # 스택에 남아있는 인덱스들은 끝까지 가격이 한 번도 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = (n - 1) - j

    return answer
# --------------------------------------------------
# 팁
# - 각 문제마다 “스택에는 무엇을, 어떤 순서로 쌓을 것인지”를 먼저 그림으로 그려 보고
# - 인덱스를 저장할지 값 자체를 저장할지 결정한 뒤
# - “새 원소가 들어왔을 때” 스택의 단조성이 깨지는 조건을 정확히 잡아 보세요.
# --------------------------------------------------
# 비슷한 문제 제시받음
# Daily Temperatures
# 설명: 하루 단위 온도 기록 T 가 주어졌을 때, 각 날짜로부터 몇 일 뒤에 더 높은 온도가 오는지 배열로 반환하세요.
# 입력 예: 
T = [73, 74, 75, 71, 69, 72, 76, 73]
# 출력 예: [1, 1, 4, 2, 1, 1, 0, 0]
from typing import List
def solution_temp(T:List[int]) -> List[int]:
    n = len(T)
    stack: List[int] =[]
    answer = [0] * n
    # day =
    for i, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)

    return answer
print(solution_temp(T))
        