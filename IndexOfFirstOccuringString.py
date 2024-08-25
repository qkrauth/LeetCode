# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part
# of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def firstStr(self, haystack, needle):

        return haystack.find(needle)

my_solution = Solution()

result = my_solution.firstStr("madbutnotsad", "sad")

print(result)


# String search/string manipulation
class SolutionTwo:
    def firstStr(self, haystack, needle):

        # Make sure needle isnt an empty string
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1): # loop over string by index, ensures loop only checks starting points in haystack that can fit (len)needle

            # check if substring matches needle
            if haystack[i:i+len(needle)] == needle: # This slices the haystack string from index i to i + len(needle)
                return i
            
        # if no matches are found
        return - 1

my_solution = SolutionTwo()

result = my_solution.firstStr("madbutnotsad", "but")

print(result)