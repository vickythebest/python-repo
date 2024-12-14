# 53. Maximum Subarray
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
def maxSubArray(self, nums: List[int]) -> int:
    largest=nums[0]
    current=0
    for n in nums:
        if n < 0:
            current=0
        current+=n
        largest=max(largest,current)
    return largest
