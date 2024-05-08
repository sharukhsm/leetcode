class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_product = 1
        right_product = 1
        ans = nums[0] 

        for i in range(len(nums)):
            # If left_product or right_product is 0, reset it to 1 to start a new product calculation
            left_product = 1 if left_product == 0 else left_product
            right_product = 1 if right_product == 0 else right_product
            # Update left_product and right_product by multiplying with the current element
            #  and its counterpart from the end of the list
            left_product *= nums[i]
            right_product *= nums[len(nums) - 1 - i] #multiplying the last element and second to the last element.
            # Update ans with the maximum of itself and the maximum product calculated so far
            ans = max(ans, max(left_product, right_product))
        # Return the maximum product found
        return ans

# Test cases
# print(maxProduct([2,3,-2,4])) # Output: 6
# print(maxProduct([-2,0,-1]))  # Output: 0
