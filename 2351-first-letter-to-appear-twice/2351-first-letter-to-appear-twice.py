class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Using a set: Time: O(n), space O(n)
        seen = set()  # Space complexity: O(n)
        for i in s:  # Time complexity: O(n)
            if i in seen:  # Time complexity: O(1)
                return i  # Time complexity: O(1)
            else:
                seen.add(i)  # Time complexity: O(1)
        # Overall time complexity: O(n)

        # Using a list: Time: O(n^2), space O(n)
        # seen = []  # Space complexity: O(n)
        # for i in s:  # Time complexity: O(n)
        #     if i in seen:  # Time complexity: O(n)
        #         return i  # Time complexity: O(1)
        #     else:
        #         seen.append(i)  # Time complexity: O(1)
        # # Overall time complexity: O(n^2)

# Using a list has a time complexity of O(n^2) due to the linear search (i in seen).
# Therefore, the implementation using a set is better in terms of time complexity.
# If the character set expands in the future to include things like upper case, symbols, accented characters, etc. 
# then the list becomes less effective. So set is future proof.