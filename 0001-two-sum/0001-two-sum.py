class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i  # mapping {key:values} to the hashtable


# since we only iterate the array once, the time complexity is O(n).
# We only need to Return the indices/index of the nums array.
# instead of x+y=target -> O(n^2), we can use this formula y=target-x, combined with hash table to devise an algorithm -> O(n).
