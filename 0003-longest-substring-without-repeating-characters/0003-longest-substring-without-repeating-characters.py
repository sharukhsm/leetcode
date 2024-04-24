class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize an empty dictionary/hash table that records 
        #the character and it's respective index as {key:value} pairs as we traverse through the string. 
        seen = {} # {char:index}

        l = 0 # set the left pointer to point at index 0 of the string
        length = 0 #length will contain the length of the longest substring.

        # loop through the string 

        for r in range(len(s)): #both l and r points at the same character initially
            char = s[r]  
            # If the character is already seen and its index is greater than or equal to the left pointer,
            # update the left pointer to the next index of the repeating character
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            # If the character is not seen or its index is less than the left pointer,
            # update the length of the longest substring if necessary
            else: 
                length = max(length, r - l + 1)
         # Update the most recent index of the current character
            seen[char] = r
        return length


# # The idea of this problem is, when we find a repeated character, 
# we move the left pointer next to the repeated character
# When a repeated character is encountered, the left pointer (l)
# is moved to the next index after the most recent occurrence of that character. 