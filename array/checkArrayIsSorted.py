def isSorted(num):
    i=num[0]
    j=1
    while j<(len(num)):
        if i>num[j]:
            print("Array is not sorted")
            return
        i=num[j]
        j=j+1
    print("Array is sorted") 



num=[1,2,3,4,4,5]
isSorted(num)