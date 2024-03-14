class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary(Hash table) to store seen elements as key and their index as value.
        seen = {}
        # Iterate through the indices of the nums list
        for i in range(len(nums)):
            # Calculate the difference needed to reach the target
            diff = target - nums[i]
            # If the difference is already seen in the dictionary
            if diff in seen:
                # Return the indices of the current element and the one that resulted in the difference
                return [seen[diff], i]
            # If the difference is not seen, store the current element and its index in the dictionary
            else:
                seen[nums[i]] = i  # mapping {key:values} to the hashtable

# Steps
# create a dictionary to store the indices
# find the difference using the formula y(diff) = target - x
# check if diff is in the dictionary, if yes return index of the dictionary and nums array [seen[diff], i]
# since we only iterate the array once, the time complexity is O(n).
# We only need to Return the indices/index of the nums array.
# instead of x+y=target -> O(n^2), we can use this formula y=target-x, combined with hash table to devise an algorithm -> O(n). 
    
 #Bruteforce solution: O(n^2)   
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

        