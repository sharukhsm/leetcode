class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num_set = set()

        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
        return False


# Create a hash set called num_set
# [1,2,3,1]
