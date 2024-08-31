# 66
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

class Solution:
    def plusOne(self, digits):

        # loop from the last element to the first
        for i in range(len(digits) - 1, -1, -1): # apparently this is the correct syntax to start at the last item in the array?

            # add 1
            digits[i] += 1

            if digits[i] < 10:
                return digits

            # otherwise set it to 0 and continue (add to the next element)
            digits[i] = 0

        # if all digits are 9 then add a 1 to the start
        return [1] + digits

my_solution = Solution()

result = my_solution.plusOne([1,2,3,9])

print(result)