# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = []
# Output: []

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head):
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
    
# create a ListNode
# initialize "previous" to be the previous node set to "None"
# "current" is the pointer of the current node initially set to the head
# use a WHILE loop to iterate through the linked list

# in the loop we create a temp value "next_node" to avoid losing the Reference
# we REVERSE the direction of the pointer by setting "current.next" to "previous"
# the loop continues until "current" becomes None which indicates we have reached the end of the original list
    
my_solution = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

reversed = my_solution.reverseList(head)

while reversed is not None:
    print(reversed.value, end = " ")
    reversed = reversed.next
