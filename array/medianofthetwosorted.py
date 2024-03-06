def findMedianSortedArrays(nums1,nums2):
    nums1.extend(nums2)
    nums1.sort()

    print("merge : ",nums1)

    mid=(len(nums1))//2
    print("mid : ",mid)
    print(nums1[mid-1],nums1[mid])

    if mid%2==0:
        return (nums1[mid-1]+nums1[mid])/2
    else:
        return nums1[mid]
    
    


    
    



nums1 = [1,2]
nums2 = [3,4]
# nums1=[1,3]
# nums2=[2]

print(findMedianSortedArrays(nums1,nums2))