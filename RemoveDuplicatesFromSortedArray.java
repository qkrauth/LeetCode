// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
// such that each unique element appears only once. The relative order of the elements should be kept the same.
// Then return the number of unique elements in nums.

public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0; // If the array is empty, then just return 0
        }

        int uniqueCount = 1;

        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // compare the current element to the previous
            if (nums[i] != nums[i - 1]) {
                nums[uniqueCount] = nums[i];
                uniqueCount++;
                // if the current element is different, its unique, so move it to the next position
            }
        }
        return uniqueCount;
    }
}
