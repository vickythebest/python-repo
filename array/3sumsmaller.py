def smaller2sum(nums,target):

    nums.sort()
    n=len(nums)
    result=set()
    for i in range(n-2):
        left=i+1
        right=n-1
        sum=nums[i]+nums[left]+nums[right]
        while left<right:
            if target<sum:
                result.add((nums[i],nums[left],nums[right]))
                left+=1
            elif target > sum:
                right-=1
            else:
                left+=1 
    return result


nums=[-2,0,1,3]
print(smaller2sum(nums,2))