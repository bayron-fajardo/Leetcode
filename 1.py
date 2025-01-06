nums = [3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
target = 6
i = 0
def sum(list,target):
    map_number = {}  
    for i in range(len(nums)):
        cur = nums[i]
        x = target - cur  
        if x in map_number:  
            return [map_number[x], i]  
        map_number[cur] = i 
            


print(sum(nums, target))