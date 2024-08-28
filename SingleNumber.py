# 136
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# XOR = xor a number with itself is 0. and xor a number with 0 you get the same number. xoring the array will cancel all numbers that repeat
class Solution:
    def singleNumber(self, nums):
        
        # initialize a result variable
        result = 0

        # loop the array
        for num in nums:

            # XOR the current number with the result
            result ^= num

        return result

my_solution = Solution()

result = my_solution.singleNumber([1,2,3,4,5,1,2,3,4])

print(result)


# Hashing problem
class SolutionTwo:
    def singleNumber(self, nums):
        
        # create a dict to store count of each number
        count = {}

        # loop and count occurencies of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        # find the number that appears once
        for num in count:
            if count[num] == 1:
                return num

my_solution = SolutionTwo()

result = my_solution.singleNumber([1,2,3,4,5,1,2,3,4])

print(result)