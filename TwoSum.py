# 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Hashmap/Dict problem
class Solution:
    def twoSum(self, nums, target):
        indicies = {}

        for i, num in enumerate(nums): # enumarate allows you to iterate both the indicies and the values of an iterable. for loop tracking 2 different things
            complement = target - num # make a complement for each num in nums

            if complement in indicies and indicies[complement] != i: # also check for duplicates. same num cant be added to itself to reach target
                return [indicies[complement], i]
            
            # if not add the num and its index to the dict indicies
            indicies[num] = i
        return None
    
my_solution = Solution()

result = my_solution.twoSum([2, 7, 11, 15], 9)

print(result)