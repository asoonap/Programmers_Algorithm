import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
# return = 2

scoville = [1,1]
# return = -1

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K :
        if len(scoville) < 2:
            return -1
        x = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville) # x2가 k보다 큰건 고려를 안하는건지 의문
        new = x + x2*2
        heapq.heappush(scoville, new)
        answer += 1
    return answer

print(solution(scoville, K))
