class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to track maximum sum and current sum
         #Initialize maximum sum with the first element of the array
        maxi = nums[0]
        # Initialize current sum
        sum = 0

        # Iterate through each element of the array
        for n in nums:
            # If the current sum becomes negative, reset it to 0,
            # as starting a new subarray with a negative sum won't yield the maximum subarray
            if sum < 0:
                sum = 0
            # Add the current element to the current sum
            sum += n
            # Update the maximum sum by comparing the current maximum with the current sum
            maxi = max(maxi, sum)
        # Return the maximum sum found
        return maxi
