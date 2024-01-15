class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        one_before_total = 1
        two_before_total = 1
        total = 0
        for i in range(2, n + 1):
            total = one_before_total + two_before_total
            two_before_total = one_before_total
            one_before_total = total
        return total
