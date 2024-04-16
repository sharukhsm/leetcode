class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length #This will return an array of 1's with len of input array
        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]

        right = nums[-1]
        for i in range(length - 2, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products


# Example 1:
# nums = [2,3,4,5]
# Create a variable length bc we'll use this a lot
# Create products array and initialize it to ones -> [1,1,1,1]
# Remember there's nothing to the left of the element at index 0 so we start our loop at index 1.
# products[i] = products[i-1] * nums[i-1]
# nums =     [2,3,4,5]
#             ↓ ↓ ↓ ↓
# products = [1,1,1,1]
# .              ↓
#            products[i] starts here

# products = [1,2,6,24]

# Next step is to calculate the products of all the numbers to the right of each index, 
# but instead of creating a new array we're just going to store the products as we go, 
# in a single variable called right and we're going to initialize the variable to the right most element 
# of the nums/the last element of nums, which is 5.

# Now we'll enter a loop that traverses backwards through the arrays.
# Lets break this down:
# for i in range(length-2, -1, -1):
# length-2 points the second to the last element of the arrays. -1 is the ending index. The last -1 is the step count.

#Now the products[i] is multiplied to the variable right and stored to products[i]. 
#(or)
#Each element in the products array is multiplied with the variable right
#Also we update the variable right, so that it gives the product of last elements of nums.

#Time and space: O(n)