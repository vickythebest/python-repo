# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

def maxArea(height):
    maxarea=0
    width=len(height)-1
    left=0
    right=len(height)-1
    while left<right:
        area=0
        if height[left]<height[right]:
            area=height[left]*width
            left+=1
        else:
            area=height[right]*width
            right-=1
        width-=1
        maxarea=max(maxarea,area)

    return maxarea

height=[1,8,6,2,5,4,8,3,7]

print(maxArea(height))
