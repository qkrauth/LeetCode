# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Two pointer
class Solution:
    def isPalindrome(self, s):
        s = s.lower()

        # remove non alphanumeric characters
        s = "".join(char for char in s if char.isalnum())

        # create pointers and check if string is equal on both sides
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
my_solution = Solution()

result = my_solution.isPalindrome("A man, a plan, a canal: Panama")

print(result)
