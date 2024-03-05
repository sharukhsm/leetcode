class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets.
        stack = []

        # Define a dictionary containing pairs of opening and closing brackets.
        pairs = {"(": ")", "{": "}", "[": "]"}

        # Iterate through each character in the input string.
        for bracket in s:
            # Check if the current character is an opening bracket.
            if bracket in pairs:
                # If it's an opening bracket, push it onto the stack.
                stack.append(bracket)

            # If it's a closing bracket:
            # - Check if the stack is empty (no matching opening bracket) / when the stack is empty and you already find a closing bracket return False.
            # - Check if the current closing bracket matches the last opening bracket.
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                # If either condition is true, the string is not valid.
                return False

        # After iterating through the entire string:
        # Check if there are any unmatched opening brackets left in the stack.
        return len(stack) == 0


# Create a stack
# Create a dictionary called pairs with the opening and corresponding closing bracket. This is how we check the brackets match up.
# create a loop with a variable called bracket to traverse the string s.
# If the bracket is an opening bracket, push it onto the stack.
# Now we check for two conditions. If either of them are True we return False.
# First condition in elif:
# If the stack is empty -> Lets say if the first bracket is a closing bracket, and the stack is already empty at this point and that means there are no more opening brackets left to close, means there is a mismatch and the string is invalid or it doesn't match the condition and we can return false.
# Second condition in elif:
# We first pop the stack and lookup the element in the key of the pairs dictionary -> pairs[stack.pop()]. Now we compare the corresponding value of the key in the pairs, If it matches the current element of the bracket, then the statement will be false, then we continue on with the loop. If the value of the pairs doesn't match up with the current element of the bracket, we return false.
# Once we are done with the loop, the stack should be empty if all the opening brackets matchup with the corresponding closing brackets after all the pops. Now we return True.

# If the last return statement is confusing, you can also use
# if len(stack) == 0:
#     return True
# else:
#     return False
