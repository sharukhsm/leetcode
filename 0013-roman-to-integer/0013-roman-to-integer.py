class Solution:
    def romanToInt(self, s: str) -> int:
        #initialize the symbols and it's values in a dictionary.
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        for i in range(len(s) - 1): #iterate until second to last character, 
        #we do this bs we compare current and next character, 
        #so at the last iteration it will check the next element and it will throw index out of bound error.
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total+= roman[s[i]]
        return total + roman[s[-1]] #We know that we are left with the last character, so just add it to total.
                 

#Roman numerals are usually written from Largest to smallerst and can just be added up.
#Exception: if a nummer is smaller than the one after it, then you subtract the smaller one.

# Logic:
#Check if the current char is less than the next character subtract the current char from the total
# If the current char is greater than the next character add the curr char to the total.

# Note:
# Why do we iterate until second to the last character?
# if the loop iterated until the last character, 
# when it tries to access s[i+1] for the last character s[-1], 
# it would result in an "index out of range" error.

# Examples:
# Roman numeral: "IX"
# "I" (1) is smaller than "X" (10) which follows it. According to the exception rule, we subtract "I" from "X".
# So, the total value is 10 - 1 = 9.

# Roman numeral: "XXIV"
# "X" (10) is followed by "X" (10), so we simply add their values.
# Then, "I" (1) is smaller than "V" (5), so we subtract "I" from total which is 19. Remember we just add the last char to the total. 
# So, the total value is 10 + 10 -1 + 5 = 24.