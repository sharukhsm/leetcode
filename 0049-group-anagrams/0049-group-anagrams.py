class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to hold grouped anagrams
        grouped = {}
        
        # Iterate through each word in the input list
        for word in strs:
            # Sort the characters in the word and join them back into a string
            sorted_word = ''.join(sorted(word))
            
            # If the sorted word is already a key in the dictionary, append the original word to the list
            if sorted_word in grouped:
                grouped[sorted_word].append(word)
            # If the sorted word is not a key in the dictionary, add it with the original word in a new list
            else:
                grouped[sorted_word] = [word]
        
        # Return the grouped anagrams as a list of lists
        return list(grouped.values())

#time complexity: O(n * m log m) time
#space: O(n * m)