# 371. Sum of Two Integers
# Attempted
# Medium
# Topics
# Companies
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5

def sum2integer(a,b):
    while b!=0:
        temp=(a&b)<<1
        a=(a^b)
        b=temp
    return a


print(sum2integer(1,2))