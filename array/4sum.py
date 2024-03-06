"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
"""

def sum4(nums,target):
    n=len(nums)
    nums.sort()
    result=set()

    for i in range(n-2):
        left=i+1
        mid=left+1
        right=n-1

        print(nums[i]," ",nums[left]," ",nums[mid]," ",nums[right])
        sum=(nums[i]+nums[left]+nums[mid]+nums[right])
        while left<right:
            if sum==target:
                print("target match")
                result.add((nums[i],nums[left],nums[mid],nums[right]))
                left+=1
                mid=left+1
            elif sum<target:
                # print("target higher then sum")
                right-=1
            else:
                # print("target lower then sum")
                left+=1
                mid=left+1
    
    print(result)
    return result


nums=[1,0,-1,0,-2,2]
print(sum4(nums,0))

# nums = [2,2,2,2,2]
# print(sum4(nums,8))