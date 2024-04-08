class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the answer variable to store the single number
        answer = 0

        # Iterate through each number in the input list
        for num in nums:
            # Using XOR operation to find the single number
            # XOR (^) operation cancels out duplicate numbers
            # and leaves only the single number in the end
            answer ^= num

        # Return the single number found after XOR operations
        return answer

# XOR logic(same nums cancells out) 

# 2^2^1 = 1
# 4^1^2^1^2 = 4