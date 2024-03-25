# leetcode - 1929
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

def getConcatenation(num):
    
    #In-build function to concate
    # num.extend(num) 
    
    k=(len(num)*2)-1
    j=len(num)
    i=0
    
    while j<=k:
        num.append(num[i])
        j=j+1
        i=i+1
    print(num)


num=[1,2,1]
getConcatenation(num)