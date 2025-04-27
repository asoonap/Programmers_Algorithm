s = ")()("
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

# 최종 제출 solution
def solution(s):
    stack = []
    for i in range(len(s)):
      if s[i] == "(":
        stack.append("(")
      else:
        if len(stack) == 0:
          return False
        stack.pop()
    if len(stack) != 0 :
      return False
    return True


# 중간과정정
def solution(s):
    stack = []
    if s[0] == ")" or s[-1] == "(":
        return False
    else:
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0 :
            return False
    return True

print(solution(s))



# 개선 solution
def solution(s):
    stack = []
    for i in s:
      if i == "(":
        stack.append(i)
      else:
        if not stack:
          return False
        stack.pop()
    return not stack

# 인덱싱 대신 직접 순회
# – for char in s: 로 간결하게

# 불필요한 len(stack) 비교 제거
# – not stack 으로 빈 스택 검사

# 조기 탈출(early exit)
# – 스택이 비어 있는데 ) 가 오면 즉시 False

# 최종 반환 간소화
# – return not stack 한 줄로 마무리