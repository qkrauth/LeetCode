# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def mergeTwoSortedLists(self, list1, list2):
        # create dummy node for simplification
        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
    
my_solution = Solution()

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

answer = my_solution.mergeTwoSortedLists(list1, list2)

while answer is not None:
    print(answer.value, end=" ")
    answer = answer.next
