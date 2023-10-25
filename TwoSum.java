// Given an array of integers nums and an integer target, return indices of the two numbers such that
// they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

import java.util.HashMap;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        // create a HashMap to store the numbers and their index
        HashMap<Integer, Integer> numIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // if the complement exists in the hashmap, return the indecies
            if (numIndex.containsKey(complement)) {
                return new int[] { numIndex.get(complement), i };
            }

            // otherwise put the current number and its index in the hashmap
            numIndex.put(nums[i], i);
        }

        return new int[0];
    }

}

// A HashMap named numIndex is created. This map will store integers as keys and their corresponding
// indices as values.
// Inside the loop, the code calculates the complement of the current number by subtracting it from the target.
// The complement represents the value needed to reach the target.
// The code checks if the complement exists in the numIndex HashMap. If it does, that means a pair of numbers
// has been found whose sum equals the target.
// If the complement doesn't exist in the HashMap, it means this number could potentially be part of a
// future pair. The code adds the current number and its index to the HashMap for later reference.
// If the loop completes without finding a solution (i.e., no pair of numbers adds up to the target),
// the code returns an empty integer array to indicate that no solution was found.