def threeSumClosest(nums, target):
    n=len(nums)
    nums.sort()
    # result=set()

    closest = (nums[0]+nums[1]+nums[n-1])
    for i in range(len(nums)):
        left=i+1
        right=n-1
        while left < right:
            sum=(nums[i]+nums[left]+nums[right])
            print("sum : ",sum, "--",abs(closest - target))
            if abs(sum-target) < abs(closest - target):
                print("less closest : ",closest)
                closest=sum

            if sum<target:
                print("left ++")
                left+=1
            elif sum > target:
                print("right --")
                right-=1
            else:
                print("return")
                return closest
    print("return : ",closest)
    return closest


nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums,target))