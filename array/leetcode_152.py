# 152. Maximum Product Subarray
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
def maxProduct(self, nums: List[int]) -> int:
    result=0
    maxnum=1
    minnum=1
    for n in nums:
        tmp=maxnum*n
        maxnum=max(maxnum*n,minnum*n,n)
        minnum=min(tmp,minnum*n,n)
        result=max(result,maxnum)
    return result