# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Two pointer technique
class Solution():
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        k = 1

        for i in range(1, len(nums)): # we use the "in range" for loop to access two different array indicies
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

my_solution = Solution()

nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]

answer = my_solution.removeDuplicates(nums)

print(answer)
