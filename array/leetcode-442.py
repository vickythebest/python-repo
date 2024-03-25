def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        temp=set()
        for i in range(len(nums)):
            if nums[i] in temp:
                result.append(nums[i])
            else:
                 temp.add(nums[i])
        print(result)
        return result

nums=[4,3,2,7,8,2,3,1]
findDuplicates(nums)