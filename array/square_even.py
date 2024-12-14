# Given an Array of integers, return an Array where every element at an even-indexed position is squared.
# Input: array = [9, -2, -9, 11, 56, -12, -3]
# Output: [81, -2, 81, 11, 3136, -12, 9]
# Explanation: The numbers at even indexes (0, 2, 4, 6) have been squared, 
# whereas the numbers at odd indexes (1, 3, 5) have been left the same.

def squareEven(arr):
    for i in range(0,len(arr),2):
        arr[i]=(arr[i]*arr[i])


array = [9, -2, -9, 11, 56, -12, -3]
squareEven(array)
print(array)