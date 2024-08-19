# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self, nums):

        # Use a set to store unique elements
        # sets CANNOT contain duplicates
        data = set()

        for num in nums:
            if num in data:
                return True # checking if the current num is inside the set
            else:
                data.add(num)
        return False

# This bottom part is necessary because we are working with a CLASS so we have to use an instance of the class to even run the code
my_solution = Solution()

result = my_solution.containsDuplicate([1, 2, 3, 3])

print(result)
