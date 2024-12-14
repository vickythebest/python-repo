"""
Given an integer array nums, return all the triplets
 [nums[i], nums[j], nums[k]] such that i != j, i != k, and 
 j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
from typing import List
def sum3(nums):
    lenght=len(nums)
    result=set()
    nums.sort()

    for i in range(lenght-2):
        print("Result :- ",result)
        left=i+1
        right=lenght-1

        while left < right: 
            
            print(f" {nums[i]}, : {nums[left]}, : {nums[right]}")
            
            sum=nums[i] +nums[left]+nums[right]
            
            if sum==0:
                result.add((nums[i] +nums[left]+nums[right]))
                left=left+1
            elif sum > 0:
                right=right-1
            else:
                left=left+1
        print("Result :- ",result)
        # unique=tuple(result)
        # print(type(unique))
        # output=set()
        # for i in unique:
        #     output.add(tuple(i))
        # print(" set = ",output)    
        
        # li=[]
        # for i in output:
        #     li.append(list(i))
        # print(" List = ",li) 

    
    return result
    


nums = [-1,0,1,2,-1,-4]
# nums=[0,0,0]
# nums=[0, 1, 1]
# output=test3sum.threeSum(nums)
# print("threeSum : ",output)

output=sum3(nums)
# print("sum3 : ",sum3(nums))