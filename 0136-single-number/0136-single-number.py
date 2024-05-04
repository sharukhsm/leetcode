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
# O(n) time and O(1) space complexity

# Example1: 
# 0^2=2
# 2^2=0
# 0^1=1

# You might have a question, what if the digits aren't sorted/next to each other? 
#The result is same because Xor is Commutative and associative.

#Note
#Any number Xor'd with 0 will result the same number. Ex: 0^2 = 2
#What is a bitwise operation? In bitwise operation, the integers are first converted into binary 
#and then operations are performed according to the type of operation. In this problem we use Xor operation. 

# Xor property aka exclusive OR
# if both bits are different return 1(true).
# if both bits are same return 0(false).

# Xor general Example:

#     1 1 0
# XOR 1 0 0
# ----------
#     0 1 0


