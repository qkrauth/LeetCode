// Roman numerals are usually written largest to smallest from left to right.
// However, the numeral for four is not IIII. Instead, the number four is written as IV.
// Because the one is before the five we subtract it making four. The same principle applies to the number nine,
// which is written as IX. There are six instances where subtraction is used

// Given a roman numeral, convert it to an integer.

import java.util.HashMap;

public class RomanToInteger {
    public int romanNumeralToInt(String s) {
        // create a hashmap to store the values of the roman numerals
        HashMap<Character, Integer> values = new HashMap<>();
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);

        int result = 0;

        // Iterate through String s or the Roman Numeral input string
        for (int i = 0; i < s.length(); i++) {
            int currentValue = values.get(s.charAt(i));

            // If the next symbol is larger, subtract the current symbols value
            if (i < s.length() - 1 && currentValue < values.get(s.charAt(i + 1))) {
                result -= currentValue;
            } else {
                result += currentValue;
            }
        }
        return result;
    }
}

// Create a hashmap to store the kay value pairs that we created to represent the roman numeral letter and
// its value
// the for loop iterates, then the .get method gets the VALUE (integer) part of the kay value pair
// The if statement checks if the end of the string has been reached, then it checks the order of the
// letters and sees if subtraction is necessary for example IV - the lower value is infront of the higher
