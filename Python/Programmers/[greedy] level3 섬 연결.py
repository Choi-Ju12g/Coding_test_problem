def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2]) # 비용기준 오름차순
    connected = set([costs[0][0]]) # 첫 시작섬 선택, 연결 확인 집합
    #print(connected)
    while len(connected) < n:
        for cost in costs:
            if cost[0] in connected and cost[1] in connected:
                continue
            elif cost[0] in connected or cost[1] in connected:
                connected.update([cost[0],cost[1]])
                #print(connected)
                answer += cost[2]
                break
    return answer

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

solution(4,costs)