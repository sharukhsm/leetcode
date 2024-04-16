class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0  # Initialize left pointer to the start of the array.
        r = len(nums) - 1  # Initialize right pointer to the end of the array.

        while l <= r:  # Perform binary search until left pointer surpasses right pointer.
            mid = (l + r) // 2  # Calculate the middle index.

            if nums[mid] < target:  # If the middle element is less than the target.
                l = mid + 1  # Move the left pointer to mid + 1.

            elif nums[mid] > target:  # If the middle element is greater than the target.
                r = mid - 1  # Move the right pointer to mid - 1.

            else:  # If the middle element is equal to the target.
                return mid  # Return the index of the target.
                
        return -1  # If the target is not found, return the index where it would be inserted.

# Time: O(log n)
# Space: (1)
#Hint: Use Binary search aalgorithm when asked to find the index of an array.

# This problem is same as leetcode 35. Search Insert Position

        