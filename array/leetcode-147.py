# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insertionSortList(nums):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    for right in range(len(nums)):
        left=right-1
        temp=nums[right]
        print(left,right,temp,nums[left-1])
        while left >-1 and nums[left] > temp:
            nums[left+1]=nums[left]
            left=left-1
        nums[left+1]=temp
    print(nums)
                  


nums=[6,5,3,1,8,7,2,4]
insertionSortList(nums)
        