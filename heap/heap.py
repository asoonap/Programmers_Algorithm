# 디스크 컨트롤러
import heapq

jobs = [[0, 3], [1, 9], [3, 5]]
return1 = 8

def solution(jobs):
    heapq.heapify(jobs)
    waiting = [] # 대기
    t = 0 # 현재 시간
    i = 0 # 인덱스
    total_wait = 0 # 총 반환 시간 
    count = 0 # 처리한 작업 수
    answer = 0
    n = len(jobs) # 전체 작업 수 
    while count < n:
        # 현재 시점 

    time = [0] * n # 3
    time_storage = [0] * n
    
    stay = [] # 대기
    go = [] # 활성화화
    while time:
        time.pop(0)
        if jobs:
            if 
        heapq.heappush(stay, heapq.heappop(jobs))
        a = heapq.heappop(stay)
    # 대기 장소 how 알맞은 시간에 집어넣기
    # 활동시간이 돌아가면서 대기 장소가 돌아가야함.

    for i in range(jobs[0][1]):
        answer += 1
        heapq.heappop(jobs)
    return answer

print(solution(jobs))

