class Solution:
    def climbStairs(self, n: int) -> int:
        #n is the number of steps
        if n == 1:
            return 1

        one_before_total = 1
        two_before_total = 1
        total_ways = 0
    # We are not using the variable i or any arrays,
    # we are just updating the variables until we reach n steps
        for i in range(2, n + 1):
            total_ways = one_before_total + two_before_total
            two_before_total = one_before_total
            one_before_total = total_ways
        return total_ways

# This can be solved using DP and we are using Bottom up approach.
# Note: this problem is just fibonacci sequence
# Example: 
# n = 3
# [1,1,2,3]  here array is just for representaion purpose.