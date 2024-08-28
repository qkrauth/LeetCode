# 350
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many
# times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution:
    def intersect(self, nums1, nums2):

        # create a dict to store the frequency of items in nums1
        count = {}

        # count occurrencies of items in nums1
        for num in nums1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # create the empty array for the result
        array = []

        # iterate through nums2 and check if the element is in the dict
        for num in nums2:
            if num in count and count[num] > 0: # repeats are allowed, thats why the item and its frequency is counted
                array.append(num)
                count[num] -= 1
        
        return array

my_solution = Solution()

result = my_solution.intersect([1,2,3,3,4], [1,3,3,4,5])

print(result)
