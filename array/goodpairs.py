# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                  if nums[i]==nums[j]:
                        count=count+1
        
        print("count",count)
                        
                        



nums=[1,2,3,1,1,3]
numIdenticalPairs(nums)