nickname = "WORLDworld"	
#"VV0RLDvv"
nickname2 = "GO"	
# "G0oo"

def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    # 1줄 수정. 
    # 길이가 4미만일 경우 소문자 o를 4가 될때까지 이어붙이기
    # 될때까지 while사용
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer


print(solution(nickname))
print(solution(nickname2))