def linearSearch(num,element):

    if element <0:
        print("Invalid elemente to search in array")
        return
    
    if len(num)==0:
        print("Array is empty")
        return

    for i in range(len(num)):
        if num[i]==element:
            print(num[i],"Elemente exit in array")
            return
    print(element,"Elemente not exit in array, Please try again")


num=[4,3,2,5,6]
print("Test 1")
linearSearch(num,-1)
print("Test 2")
linearSearch([],1)
print("Test 3")
linearSearch(num,6)