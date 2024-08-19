# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# String manipulation
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        # Use dictionaries to store characters
        s_count = {}
        t_count = {}

        # Lets compare
        # These dicts are used to keep track of the count or frequency of each char. Like how many times a specific char appears in the string. the 0 param is only there for if
        # char does not have a value yet and the + 1 keeps track of the count I suppose
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        return s_count == t_count
    
my_solution = Solution()

result = my_solution.isAnagram("silent", "tensil")

print(result)
