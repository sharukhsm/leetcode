class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # (python default int size is not 32bit, it is very large 
        # number, so to prevent overflow and stop running into infinite loop, 
        # we use 32bit mask to limit int size to 32bit

        # Iterate until there is no carry left, b holds the carry value.
        while (b & mask > 0):
            # Calculate the carry and Left shift by 1
            # And(&): both bits should be true/1 to return 1, else 0
            # Left shift by 1 simulates the carry operation in binary addition.
            carry = (a & b) << 1
            
            # Calculate the sum without carry using XoR. 
            # XOR: both bits should be different to return true/1, else 0
            a = a ^ b
                
            b = carry

        # Return final sum
        return (a & mask) if b > 0 else a
        

# When you are asked to do any arithmetic operations without any signs(+-*/)
# then you can solve those problems with Bit manipulation.

# How to find binary representation of a number
# What's the binary representation of 13?
# 13/2 = 6, remainder = 1
# 6/2 = 3, remainder = 0
# 3/2 = 1, remainder = 1
# 1/2 = 0, remainder = 1
# Reading the remainders from bottom to top gives the binary representation: 1101.
# So the binary rep of 13 is 1101

# Normal Binary addition with + operator.
# Adding binaries of 123 + 39      
#       1 1 1 1 1 1 1   <-(carry)
#         1 1 1 1 0 1 1   (123)
#      +    1 0 0 1 1 1   (39)
#      -----------------
#       1 0 1 0 0 0 1 0
#      -----------------          2 = 10
#                                 3 = 11

# Steps:
# So to add two binaries we need carry, so first calculate carry.
# Carry can be calculated using &
# Now add a and b without carry, this can be done using XOR
# Finally left shift the carry by 1

# Example 1:
# Binary Representation:
# a = 1: Binary representation is 001.
# b = 2: Binary representation is 010.
# Iteration 1:
# carry = a & b: 001 & 010 = 000 (no common bits set).
# a = a ^ b: 001 ^ 010 = 011 (XOR operation gives the sum without considering carry).
# b = carry << 1: carry = 000, shift left by 1 bit gives 000.
# b = 0
# a = 011 (3)
# Iteration 2:
# Since b is 0, so we end the loop and return a.
# therfore a = 3 