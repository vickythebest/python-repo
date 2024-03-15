# Insert elements in sorted array 

def insertElement(num,element):
    for i in range(len(num)):
        if num[i]<element:
            num.insert(i+1,element)
            return num

   




num=[1,3,5,6,8]



print(insertElement(num,2))
print(insertElement(num,0))
# insertElement(num,4)
# insertElement(num,7)
# insertElement(num,0)

    # while l<=r:
    #     mid=(l+r)//2
    #     if num[mid]>element:
    #         num.insert(mid,element)
    #         r=mid-1
    #         return num
    #     else:
    #         l=mid+1

    # print("new array : ",num)