class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        
        # Stop the loop when L = R, bc we found the pivot
        while L < R:
            M = (L + R) // 2
            # If the value at middle index is greater than the value at right pointer, then
            # the pivot point lies to the right of middle, so adjust left pointer accordingly
            if nums[M] > nums[R]:
                L = M + 1
            # if nums[M] < nums[R], the pivot point lies to the left of or at middle, 
            # so adjust right pointer    
            else:           
                R = M
        # At the end of the loop, left pointer points to the minimum element/pivot 
        # We return either L or R bc they are equal to each other           
        return nums[L]


# Note
#If the array is sorted and the problem asks for O(log n) time, 
# this just shouts the problem can be solved using Binary search.


#Basic approach(first intuition)
        # nums.sort()
        # return nums[0]

    #Bruteforce O(n)
    # def findMin(self, nums: List[int]) -> int:
    #     min_num = float('inf')
    #     for num in nums:
    #         min_num = min(min_num, num)
    #     return min_num