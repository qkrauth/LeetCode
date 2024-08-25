# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):

        # dictionary to store the last seen index of each character
        char_index = {}

        # initialize pointers and max length variable
        left = 0
        max_length = 0

        # loop through string s with right pointer
        for right in range(len(s)): # in range allows looping over the string by index
            if s[right] in char_index and char_index[s[right]] >= left:
                # move left pointer to the right of the last occurance of character
                left = char_index[s[right]] + 1

            # update last seen index of current character
            char_index[s[right]] = right

            # calculate current length of substring
            max_length = max(max_length, right - left + 1)

        return max_length

my_solution = Solution()

result = my_solution.lengthOfLongestSubstring("abcdeabcde")

print(result)