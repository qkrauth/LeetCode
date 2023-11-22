import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        // create a "stack" to store opening brackets
        Stack<Character> stack = new Stack<>();

        // iterate through String s
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            // check if the current character is an opening bracket
            if (c == '(' || c == '{' || c == '[') {
                // push opening brackets onto the stack
                stack.push(c);
            } else {
                // if stack is empty (no matches)
                if (stack.isEmpty()) {
                    return false;
                }

                // pop the top element from the stack
                char top = stack.pop();

                // check if the popped bracket matches the current closing bracket
                if (c == ')' && top != '(' || c == '}' && top != '{' || c == ']' && top != '[') {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}

// Stacks are good to maintain LIFO or first-in-last-out, making it suitable for scenarios when the order
// of elements matter

// create a Stack<Character> to store opening brackets
// Iterate through the string and if the i is an opening bracket we push it onto the stack
// If i is a closing bracket we check for the following: If the stack is empty return false cuz there
// is nothing to match. pop the top element from the stack and see if it matches the current closing bracket
// runtime is O(n) stack operations are constant time and (n) is String length we are iterating
