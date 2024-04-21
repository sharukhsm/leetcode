class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1 #start from last character of the string

        # Skip trailing spaces
        while i>=0 and s[i] == ' ': 
               i-=1
        # Calculate the length of the last word
        while i>=0 and s[i] != ' ':
            length+=1
            i-=1
        # Return the length of the last word   
        return length
