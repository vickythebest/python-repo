def calculateMaxarea(arr):
    print('calculate', arr)
    i=0
    j=len(arr)-1
    width=len(arr)
    result=0
    while i<j:

        print('current width',width, 'I :',i,'J :', j)
        if arr[i]==arr[j]:
            multiple =width* arr[i]
            if result<multiple:
                result=multiple
            i=i+1
            width=width-1
            print('multiple = ',multiple,'result in elif',result)
            j=j-1
            i=i+1
        elif arr[i]<arr[j]:
            multiple =width* arr[i]
            if result<multiple:
                result=multiple
            i=i+1
            width=width-1
            print('multiple = ',multiple,'result in elif',result)
        else:
            multiple =width* arr[j]
            if result<multiple:
                result=multiple
            j=j-1
            width=width-1
            print('multiple = ',multiple,'result in else',result)
    print(result)


arr=[1,8,2,4,6,8,7]
calculateMaxarea(arr)