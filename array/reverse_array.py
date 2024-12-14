def reverse(nums):
    left=0
    right=len(nums)-1

    while left < right:
        temp=nums[right]
        nums[right]=nums[left]
        nums[left]=temp
        left+=1
        right-=1
    
    print(nums)

nums=[9,8,7,6,5,4,3,2,1]
reverse(nums)