# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number nine,
# which is written as IX. There are six instances where subtraction is used

# Given a roman numeral, convert it to an integer.

# String manipulation
class Solution():
    def romanToInt(self, s):

        # create dict to store values to roman lettering
        roman_num_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        total = 0
        previous_value = 0

        for char in reversed(s): # REVERSED allows us to iterate through the string BACKWARDS. can be useful!
            current_value = roman_num_dict[char]

            # if the current value is less than the previous one, we will have to subtract it. ex: IX will be 9 and the right-most letter equates to a 10
            if current_value < previous_value:
                total = total - current_value

            else:
                total = total + current_value
            
            previous_value = current_value # this updates the previous value for the next iteration
        
        return total
    
my_solution = Solution()

answer = my_solution.romanToInt("IL")

print(answer)
