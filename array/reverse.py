def reverse(num):
    l=0
    r=len(num)-1
    
    while l<=r:
        temp=num[r]
        num[r]=num[l]
        num[l]=temp
        l=l+1
        r=r-1
    print(num)

num=[8,7,6,5,4,3,2,1]
reverse(num)