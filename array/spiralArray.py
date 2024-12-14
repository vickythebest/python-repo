def spiralclockwise(matrix):

    left,right=0,len(matrix[0])-1
    top,bottom=0,len(matrix)-1
    result=[]
    print(f"top :{top}, right :{right}, left :{left} , bottom : {bottom}")
    while left <= right and top <= bottom:
        for i in range(left,right+1):
            result.append(matrix[top][i])
            # print("row",matrix[top][i])
        top+=1
        
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
            # print("col",matrix[i][right])
        right-=1

        if top <= bottom:
            for i in range(right,left-1,-1):       
                # print("row2",matrix[bottom][i])
                result.append(matrix[bottom][i])
            bottom-=1

        if left <= right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
                # print("col2",matrix[i][left])
            left +=1

        # print("End : ")    
    print("result : ",result)
        # print(f"count : {count} top :{top}, right :{right}, left :{left} , bottom : {bottom}")
#           top :0, right :4, left :0 , bottom : 4
# count : 1 top :0, right :5, left :1 , bottom : 4

matrix=[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

spiralclockwise(matrix)