# Codesignal problem
# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.
# Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag.
#  More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1
# if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

# Example

# For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].

# (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
# (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
# (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;

class Solution:
    def zigzagArray(self, numbers):

        newArray = [] # create the new array to return

        for i in range(len(numbers) - 2): # loop only a certain amount of times (5 - 2 = 3)

            a = numbers[i]
            b = numbers[i + 1] # create variables so easier to track
            c = numbers[i + 2]

            if (a < b > c) or (a > b < c): # make the comparisons
                newArray.append(1)
            else:
                newArray.append(0)
        
        return newArray

my_solution = Solution()

result = my_solution.zigzagArray([1, 2, 1, 3, 4])

print(result)