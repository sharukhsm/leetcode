class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Initialize a variable to track the position to overwrite non-val elements
        for x in nums:  # Iterate through each element x in the list nums
            if x != val:  # Check if the current element is not equal to val
                nums[i] = x  # Overwrite the current element at position i with x
                i += 1  # Increment the position tracker i
        return i  # Return the final value of i, representing the length of the modified nums list


#Note:
# In this problem you aren't just returning i. You're also modifying the existing array.

      
        