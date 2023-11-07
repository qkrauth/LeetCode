// Given an integer x, return true if x is a palindrome and false otherwise.

public class PalindromeNumber {

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false; // negative numbers cannot be palindromes
        }

        // convert the integer to a string
        String strNum = String.valueOf(x);

        // compare the original string with the reverse
        return strNum.equals(new StringBuilder(strNum).reverse().toString());
    }
}

// The .equals part at the end basically returns true or false, that's the logic in this question.
// return type then true if the strNum reverse equals strNum
