def union(num1,num2):
    result=[]
    for i in range(len(num1)-1):
        for j in range(len(num2)-1):
            if num1[i]==num2[j]:
                result.append(num1[i])

    print(result)

a1=[2,3,4,5]
a2=[1,2,3,4]
union(a1,a2)