class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        num_set = set()  # Create an empty set called num_set

        for num in nums:
            if num in num_set:  # check if num is in num_set
                return True
            else:  # if num is not in num_set, add num to num_set
                num_set.add(num)  
        # If the for loop completes without finding duplicates, return False.
        return False


# In python hashsets are called sets.
# We use sets because they can be used to store unique items.
