def sum_zero(nums):
    ## return two value that sums to 0
    ## sumZero([-4,-2,0,3,4,5]) => [-4, 4]
    ## sumZero([-4,1,3]) => undefined
    
    ## first use for...in to iterate nums[i] <= i = 0
    ## then nested loop to iterate nums[j] <= j = len(nums) - 1
    ## if nums[i] + nums[j] === 0 then return i,j
    ## if not, j+=1
    ## i+=1
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 0:
                print(i, j)
                return i, j
        
    print("none")
    return None
    

sum_zero([-4,-2,0,3,4,5]) 
# sum_zero([-4,1,3])
    
    