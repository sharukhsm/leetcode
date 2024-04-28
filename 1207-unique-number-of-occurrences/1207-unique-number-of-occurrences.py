class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Create a Counter object to count occurrences and store it in a variable called counter.
        counter = Counter(arr) #{num: frequency}
        
        # Create an empty set to store unique frequencies
        s = set()
        
        for num_freq in counter.values():  # Iterate over the frequencies of elements in counter
            # If the current frequency num_freq is already in set s,
            # it means there are duplicate occurrences of the same frequency
            if num_freq in s:
                return False
            else:             # Otherwise, add the current frequency v to set s
                s.add(num_freq)
        #If the loop is complete that means there are no duplicates and we return true.
        return True


# Python Counter class is part of Collections module. Counter is a subclass of Dictionary 
# and it's used to keep track of elements and their count.
# Python Counter takes in input a list, tuple, dictionary, string, 
# which are all iterable objects, and it will give you output that 
# will have the count of each element in {key:value} pairs.

# Example 1:
# counter = Counter(arr) 
# ['1': 3,'2': 2,'3': 1] #nums and their frequencies.

#counter.values() extracts the frequencies

#Time and space: O(n)
#Fun fact: this is an apple coding question