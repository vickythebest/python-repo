def binarySearch(num,element):
    start=0
    end=len(num)-1
    
    while start <= end:
        mid=(end+start)//2
        
        if num[mid]==element:
            print(num[mid],"Element found at index : ",mid )
            return
        elif element < num[mid]:
            end=mid-1
        else:
            start=mid+1

        # print("start",start)
        # print("mid",mid)
        # print("end",end)
    print(element,"Element not found")

num=[1,3,4,5,6]
print("Test 1")
binarySearch(num,1)
print("Test 2")
binarySearch(num,3)
print("Test 3")
binarySearch(num,4)
print("Test 4")
binarySearch(num,5)
print("Test 5")
binarySearch(num,6)
print("Test 6")
binarySearch(num,9)