def solution (r = int(), c = int()):
    #we need to go for (r-1)+(c-1) = r+c-2 times, which is the size of a list of "going"
    #and r-1 of the movements in the list is "going down"
    #and the rest place are filled with "going right"
    #so solution = (r+c-2)!/(r-1)!(c-1)!
    #which is (r+c-2)/(r-1) 
    return (r+c-2)*(r-1)

print(solution(3,3))
print(solution(2,2))

#or we can use iteration
"""
def solution (r = int(), c = int()):
    gird_list=[][]

"""