# 같은 숫자는 싫어
arr = [1, 1, 3, 3, 0, 1, 1]
arr2 = [4, 4, 4, 3, 3]

def solution(arr):
    answer = []
    for i in range(len(arr)):
        # 빈 리스트면 추가, 중복이 아니면 추가
        if len(answer) == 0:
          answer.append(arr[i])
        else: 
          if answer[-1] != arr[i]:
             answer.append(arr[i])
    return answer

print(solution(arr))
print(solution(arr2))


# stack 선입후출
## 리스트 자료형을 사용하여 구현
### append 리스트의 가장 뒤쪽에 삽입
### pop  리스트의 가장 뒤쪽에서 데이터를 꺼냄

# queue 선입선출