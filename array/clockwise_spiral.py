"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
"""

# def __init__(self) -> None:
#     pass


def spiral(matrix):
    print("Clockwise spiral")
    left, right=0,len(matrix[0])-1
    top,bottom=0,len(matrix)-1


    while left <= right and top <= bottom:
        # print("print matrix Clockwise spiral ")
        for i in range(left,right+1):
            print(matrix[left][i])
        left +=1
                
        for i in range(top,bottom):
            print(matrix[i][right])
        right -=1

        if top <= bottom:
            for i in range(left,right+1):
                print(matrix[left][i])

        if left < right:
            for i in range(left,right+1):
                print(matrix[left][i])

        
        


matrix=[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

spiral(matrix)