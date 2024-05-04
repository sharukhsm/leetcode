class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer approach. Initialize left and right pointers
        l = 0
        r = len(height) - 1
        max_area = 0

        # Loop until the left pointer equals the right pointer
        while l < r:
           # w = r - l calculates the distance between the rightmost and leftmost bars.
           # r - l bc we need a positive value, remember we're only using index to find the width.
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a)
    # Here we need to skip the shorter bar to find the maximum area to potentially find 
    # the maximum area, so we need to move eith L or R pointers. 
    # depending on which bar is shorter.
            if height[l] < height[r]:
                l+=1
    # If height[l] >= height[r], it means that the height of the leftmost bar  is greater than 
    # or equal to the height of the rightmost bar. In this case, moving the right pointer (r)
    # towards the left could potentially lead to finding a greater area.
            else:
                r-=1
        return max_area
        


# Note: 
# To find the width you might ask why w = r - l is used instead of l - r:
# Directionality: In a typical Cartesian coordinate system where the x-axis increases 
# from left to right, Subtracting the index of the rightmost bar 
# from the index of the leftmost bar (r - l) aligns with this directionality,
# producing a positive value for the width.

# Steps:
# Two Pointers: Use two pointers starting from both ends of the array.
# Maximize Area: Maximize the area by considering the shorter bar and the width between the bars.
# Move Pointers: Move the pointer skipping the shorter bar inward to find max area.
# Update Max Area: Keep track of the maximum area encountered.
# Terminate: Stop when the pointers converge.

# Area formula:
# Area = W x H
# W = L - R (difference btw the indices)
# H = min(height[l], height[r]) (minimum bar)