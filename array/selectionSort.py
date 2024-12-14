def selectionSort(nums):

    # left=0
    # right=0
    # index=0
    # n=len(nums)
    # while index < n:
    #     while right < n :
    #         if nums[right]<nums[left]:
    #             left=right
    #         right=right+1
    #     temp=nums[index]
    #     nums[index]=nums[left]
    #     nums[left]=temp
    #     index=index+1
    #     left=index
    #     right=index
    #     # print(index,left,right ,nums)
    #     # return    
    # print(index,left,right ,nums)
        
    
    for  i in range(len(nums)):
        min_index=i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
        print(nums)
        break
    


    # for i in range(len(nums)-1):
    #     n=len(nums)
    #     temp=nums[i]
    #     left=i
    #     right=i+1
    #     print(nums[left],nums[right])
    #     while right < n and nums[right]<nums[left]:
    #         left=right
    #         right=right+1
    #         print(i,left,right)
    #     nums[i]=nums[left]
    #     nums[left]=temp
    #     print(i,left,right ,nums)
    #     return
        
    # print(nums)

nums=[8,6,3,2,5,4]
selectionSort(nums)