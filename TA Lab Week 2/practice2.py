def solution (n=int, List=list):
    min_stair_cost_list = [100000]*(n+1)
    min_stair_cost_list[0] = 0
    min_stair_cost_list[1] = List[0]

    for i in range(2, n+1):
        min_stair_cost_list[i] = min(min_stair_cost_list[i-1]+List[i], min_stair_cost_list[i-2]+List[i-1]) 
        print(i ,min_stair_cost_list[i])
    
    return min_stair_cost_list[n]

print(solution(9, [1,100,1,1,1,100,1,1,100,1]))