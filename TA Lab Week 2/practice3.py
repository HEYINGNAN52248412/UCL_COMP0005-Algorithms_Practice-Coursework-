def solution(List=list, n=int):
    left = 0
    right = len(List)-1
    
    max_position = -1
    find_num = 0

    while (left <= right):
        mid_point = (right+left)//2
        if List[mid_point] > List[mid_point-1] and List[mid_point] > List[mid_point+1]:
            max_position = mid_point
            break
        elif List[mid_point] < List[mid_point-1]:
            right = mid_point-1
        elif List[mid_point] > List[mid_point-1]:
            left = mid_point+1
        

    left_left = 0
    left_right = max_position
    

    while (left_left <= left_right):
        left_mid_point = (left_left+left_right)//2
        if List[left_mid_point] == n:
            find_num = 1
            return find_num 

        if List[left_mid_point] > n:
            left_right = left_mid_point-1

        if List[left_mid_point] < n:
            left_left = left_mid_point+1

    right_left = max_position
    right_right = len(List)-1
    


    while (right_left <= right_right):
        right_mid_point = (right_left+right_right)//2
        if List[right_mid_point] == n:
            find_num = 1
            return find_num 

        if List[right_mid_point] > n:
            right_right = right_mid_point-1

        if List[right_mid_point] < n:
            right_left = right_mid_point+1

    return find_num

print(solution([2,4,6,8,10,12,11,9,7,5,3], 8))

        