# leetcode - 1920
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# Example 1:

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
def buildArray(nums):
    n=len(nums)
    # print("length",n)
    for i in range(len(nums)):
        newvalue=nums[i]%n
        print("newvalue : ",newvalue)
        current=nums[nums[i]]%n
        print("current : ",current)
        nums[i]=newvalue+(current*n)
        print(nums)
    for i in range(len(nums)):
        nums[i]=nums[i]//n
    print(nums)
# def buildArray(nums):
#     i=0
#     visit=set()
#     while i < len(nums):
#         temp=nums[i]
#         visit.add(i)
#         print(i,temp,nums[nums[i]])
#         nums[i]=nums[nums[i]]
#         if temp not in visit:
#             nums[temp]=temp
#         i=i+1

#         print(nums)

def buildArraybasic(nums):
    result=[]
    for i in range(len(nums)):
        result.append(nums[nums[i]])

    print(result)
nums = [0,2,1,5,3,4]
buildArray(nums)
# buildArraybasic(nums)


