class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        # Using a set: Time: O(n), space O(n)
        
        seen = set()  # Space complexity: O(n)
        for i in s:  # Time complexity: O(n)
            if i in seen:  # Time complexity: O(1)
                return i  # Time complexity: O(1)
            else:
                seen.add(i)  # Time complexity: O(1)


        # Using a list: Time: O(n^2), space O(n)
        
        # seen = []  # Space complexity: O(n)
        # for i in s:  # Time complexity: O(n). The in operator on a Python  list is O(n)
        #     if i in seen:  # Time complexity: O(n)
        #         return i  # Time complexity: O(1)
        #     else:
        #         seen.append(i)  # Time complexity: O(1)

        
        # Using a dictionary: Time: O(n), space O(n)
        
        seen = {}  # Space complexity: O(n)
        for i in s:  # Time complexity: O(n)
            if i in seen:  # Time complexity: O(1) average case
                return i  # Time complexity: O(1)
            else:
                seen[i] = True  # Time complexity: O(1)

# The time complexity of using a list is O(n^2) because the in operator on a Python list is O(n).
# which performs a linear search, and has a time complexity of O(n).
# Therefore, the implementation using a set is better in terms of time complexity.
# Both has same space complexity: O(n)
# If the character set expands in the future to include things like upper case, symbols, accented characters, etc. 
# then the list becomes less effective. So using a set/dictionary is future proof.