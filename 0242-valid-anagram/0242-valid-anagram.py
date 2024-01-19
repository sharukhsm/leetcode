class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        return s_freq == t_freq

# Comparing dictionaries in python compares the contents of the dictionary. ie. it compares the key, value pairs of the dictionary.


# initialize two empty dictionaries
# Loop through the string

# Example1: s= 'loop', t = 'polo'
# s_freq[l] = s_freq.get(l, 0) + 1

# s_freq[l]  this line adds l as the key value to the dictionary.
# s_freq.get(l, 0) + 1  this line returns either 0 or 1.
# It basically checks if the char l is in the dict, if Yes: value of the dict is added to + 1, if not the value is 0.

# The get method gets the key as the 1st argument. The second argument is returned if the given key doesn't exist.

# s_freq.get(l, 0) + 1 : returns 0 since l isn't in the string and + 1 is added.
# Now s_freq[l] = s_freq.get(l, 0) + 1
# s_freq[l] = 0 + 1
# s_freq[l] = 1
# s_freq[l] = {l : 1}

# s_freq[char] =
# {
#     l : 1
#     o : 2
#     p : 1
# }

# t_freq[char] =
# {
#     l : 1
#     o : 2
#     p : 1
# }
# return s_freq == t_freq
# Output -> true
