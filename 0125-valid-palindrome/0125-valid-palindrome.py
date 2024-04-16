class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize start and end values of the string
        l = 0
        r = len(s) - 1
        
        # loop until two pointers meet in the middle
        while l<r:
        # here we are basically ignoring whitespaces, and non alphanumerica characters.
        #isalnum checks if the string is alphanumerric.
        #if the string is not alphanumeric move to the next character
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            #if both are same increment l and decrement r, and check next character.
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            # if l and r aren't same return False
            else:
                return False
        return True

# Time:O(n)
# Space: O(1)
