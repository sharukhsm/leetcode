class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if n is positive and if 3**19 is divisible by n
        if n>0 and 3**19%n == 0:
            return True

# You can also write this 
# return n>0 and 3**19%n == 0
        
        