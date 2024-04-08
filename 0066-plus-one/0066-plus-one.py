class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate through the digits list in reverse order
        for i in reversed(range(len(digits))):
            # If the current digit is not 9, simply add 1 to it
            if digits[i] != 9:
                digits[i] += 1
                return digits  # Return the updated digits
            # If the current digit is 9, set it to 0 and continue
            digits[i] = 0
        # If all digits are 9, append 1 to the beginning of the list
        return [1] + digits

    #O(n) time and space complexity