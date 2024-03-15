def findMax(num):
    max=num[0]
    for i in range(len(num)):
        if num[i]>max:
            max=num[i]
    
    print("Max ", max)


num=[11,3,4,5,6,8]
findMax(num)