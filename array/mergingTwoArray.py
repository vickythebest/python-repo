def mergeArray(num1,num2):
    i=0
    j=0
    result=[]

    while i<=len(num1)-1 and j <= len(num2)-1:

        if num1[i]<num2[j]:
            result.append(num1[i])
            # print("-",result)
            i=i+1    
        else:
            result.append(num2[j])
            # print("=",result)
            j=j+1
    while i < len(num1):
        result.append(num1[i])
        i=i+1

    while j < len(num2):
        result.append(num2[j])
        j=j+1
    
    print(result)

a1=[2,3,4,5,9]
a2=[1,2,3,4,6,10]
mergeArray(a1,a2)

# 1,2,2,3,3,4,4,5