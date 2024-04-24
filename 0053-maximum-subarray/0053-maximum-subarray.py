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


#Sliding window approach(Algoengine)
    # def maxSubArray(nums):
    #     curr_max = 0
    #     overall_max = float('-inf')
    #     for num in nums:
    #         curr_max = max(curr_max + num, num)
    #         overall_max = max(overall_max, curr_max)
    #     return overall_max
