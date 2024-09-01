# 383
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine
# and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:


# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote, magazine):

        # create dict to count chars in magazine
        char_count = {}

        # count each char in magazine
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1 # the .get(chat, 0) - 0 if the default value of char incase it doesnt yet exist

        # check each char in randomNote compared to char_count (magazine count)
        for char in ransomNote:
            # if the character is not in magazine or used up, return false
            if char not in char_count or char_count[char] == 0:
                return False
            # else decrement the count of the char that was just counted
            else:
                char_count[char] -= 1

        return True

my_solution = Solution()

result = my_solution.canConstruct("tomfy", "tomfoolery")

print(result)