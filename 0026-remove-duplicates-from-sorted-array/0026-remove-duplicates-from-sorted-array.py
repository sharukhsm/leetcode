class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace = 1  # Initialize a variable to track the position for placing non-duplicate elements

        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[i-1] != nums[i]:
                # If it is different, update the next position for placing the non-duplicate element
                nums[replace] = nums[i]
                replace += 1  # Move the pointer to the next position
        return replace  # Return the updated length of the list with duplicates removed
