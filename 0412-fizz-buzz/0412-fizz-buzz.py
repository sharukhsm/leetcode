class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Initialize an empty list to store the FizzBuzz results
        result = []
        
        # Iterate over numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Check if the current number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                # If divisible by both 3 and 5, append "FizzBuzz" to the result list
                result.append("FizzBuzz")
            # Check if the current number is divisible by 3 only
            elif i % 3 == 0:
                # If divisible by 3 only, append "Fizz" to the result list
                result.append("Fizz")
            # Check if the current number is divisible by 5 only
            elif i % 5 == 0:
                # If divisible by 5 only, append "Buzz" to the result list
                result.append("Buzz")
            else:
                # If not divisible by either 3 or 5, append the number as a string to the result list
                result.append(str(i))
        
        # Return the list containing the FizzBuzz results
        return result
        
# Time and space: O(n)

# Note: if you don't check the divisibility of 3 and 5 as the first condition, 
# By checking both divisibility by 3 and 5 together first, 
# we ensure that a number like 15 is correctly labeled as "FizzBuzz"
#  instead of incorrectly labeled as "Fizz" or "Buzz" individually.