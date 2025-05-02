# 다리를 지나는 트럭
# --------------------------------------------------
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
# 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 
# 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
# --------------------------------------------------

#
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# answer = 8
#
# bridge_length = 100
# weight = 100
# truck_weights = [10]
# answer = 101
#
# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
# answer = 110
# --------------------------------------------------

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    while bridge:
        time += 1
        # print(f'다리 현황: {bridge}')
        bridge.pop(0) #한칸씩 전진, 새로 올리기기
        if truck_weights:
          print(f'트럭 대기: {truck_weights}')
          if sum(bridge)+truck_weights[0] <= weight: # 가능 무게보다 작을때 bridge 들어가게함
            passing = truck_weights.pop(0)
            bridge.append(passing)
            # print(f'트럭 진입: {passing}, 다리 현황: {bridge}')
          else:
            bridge.append(0)
            print('트럭 진입 실패, 한칸 전진')
    return time

print(solution(bridge_length, weight, truck_weights))

# --------------------------------------------------
# 시간 초과와 씨름하다 구글링을 하게되어 좋은 답안을 본 상황...
# deque와 list 모두 구현해봐야하는듯
# --------------------------------------------------

# deque
from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution_deque(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights)
    bridge_weights = 0
    time = 0
    while len(truck_weights) != 0:
       time += 1
       bridge_weights = bridge_weights - bridge.popleft()

       if bridge_weights + truck_weights[0] <= weight:
          bridge_weights += truck_weights[0]
          bridge.append(truck_weights.popleft())
       else:
          bridge.append(0)
    time = time + bridge_length
    return time

print(solution_deque(bridge_length, weight, truck_weights))

