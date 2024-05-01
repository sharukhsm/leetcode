class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for freq in counter.values():
            # If the frequency of any element is greater than 2, it's not possible to split
            # the list into two subarrays with equal frequency of each element
            if freq > 2:
                return False
        # If no element has a frequency greater than 2, it's possible to split the list
        return True


# The goal of the problem is to check if the array can be split into two subarrays with even length 
#and we are not checking if the values are same.
# You don't have to actually split the array, you only check if it's possible. 
# So if any of the elements freq is > 2 it's not possible to split the array equally
# Remember, the input array is in even length, so this is not a valid test case [1,2,2,3,4], bc length = 5.