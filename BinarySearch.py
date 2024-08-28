# 704
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# this is LINEAR SEARCH
class Solution:
    def search(self, nums, target):

        for i, num in enumerate(nums): # we use ENUMERATE to iterate over the elements of 'nums' along with their indicies 'i'
            if num == target:
                return i
            else: # this else code block can also be left out
                continue
        
        return -1
    
my_solution = Solution()

answer = my_solution.search([-1, 0, 3, 5, 9, 12], 9)

print(answer)


# HERE IS BINARY SEARCH ALGORITHM CODED FOR THIS PROBLEM
# divide the search interval in half repeatedly

class Solution:
    def binarySearch(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # finds the middle index

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # moves to the right half
            else:
                right = mid - 1 # moves to the left half
        
        return -1
    
my_solution = Solution()

answer = my_solution.binarySearch([-1, 0, 3, 5, 9, 12], 9)

print(answer)
