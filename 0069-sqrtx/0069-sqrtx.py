class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize left and right pointers for binary search
        left = 0
        right = x
        #Perform binary search
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid *mid
            # If square of mid is less than x, update left pointer
            if mid_squared < x:
                left = mid + 1
            # If square of mid is greater than x, update right pointer
            elif mid_squared > x:
                right = mid - 1
            else:  # if mid*mid = x
                return mid
# If exact square root not found, return integer part of square root.
#if the exact square root isn't found, 
#returning right ensures that the function returns the 
#closest integer that is less than or equal to the square root of x.
        return right

# Time complexity: O(log N)
# Space: O(1)