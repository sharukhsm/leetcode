class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a)
    # Now we need to move eith L or R pointers. 
    # When we do this we need to keep the bigger bar 
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area
        









        # Area = W x H
        # W = L - R (difference btw the indices)
        # H = min(height[l], height[r]) (minimum bar)