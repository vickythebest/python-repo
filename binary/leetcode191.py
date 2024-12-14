# Given a positive integer n, write a function that returns the number of 
# set bits
#  in its binary representation (also known as the Hamming weight).
# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.
# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit
def hammingWeight(n):
    result=0
    while n:
        result+=n%2
        n=n//2
    return result

print(hammingWeight(3))
print(hammingWeight(11))
