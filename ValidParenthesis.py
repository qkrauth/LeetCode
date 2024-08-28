# 20
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true

# Stack based problem
class Solution:
    def isValid(self, s):
        # lets use a STACK to keep track of opening brackets. A stack is good because it has LIFO properties
        stack = []

        # define a mapping of opening to closing brackets
        bracket_mapping = {")": "(", "}": "{", "]": "["} # dictionary

        for char in s:
            if char in bracket_mapping.values(): # checks if char is an opening bracket
                stack.append(char)
            elif char in bracket_mapping.keys(): # checks if char is a closing bracket
                if not stack or stack.pop() != bracket_mapping[char]: # .pop removes and returns value at the LAST index (-1)
                    return False 
            else:
                return False
        
        return not stack # if stack is empty, all brackets were matched/closed properly
        # NOT STACK = means empty stack

my_solution = Solution()

result = my_solution.isValid("(){}([])")

print(result)
