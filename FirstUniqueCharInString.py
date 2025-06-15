# 387
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0

# Example 2:

# Input: s = "loveleetcode"
# Output: 2

class Solution:
    def firstUnique(self, s):

        # create a dict to count occurances
        count = {}

        # loop to count all characters
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # second loop, first character with a count of 1 exactly
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
            
        return -1
    
my_solution = Solution()

result = my_solution.firstUnique("leetcodeisliterallyasslmao")

print(result)