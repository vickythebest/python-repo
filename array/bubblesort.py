
def bubbleSort(nums):
    n=len(nums)
    count=0  # Count to check whether bubble sort is adoptive or not
    for i in range(n):
        
        for j in range(n-1):
            
            if nums[j]>=nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                count=count+1
                print(nums)
    print(count)
        

nums=[8,5,7,2,3]
# nums=[2, 3, 5, 7, 8]  # Sorted array to check whether bubble sort is adoptive or not
bubbleSort(nums)