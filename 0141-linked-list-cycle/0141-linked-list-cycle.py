# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, to the head of the linked list.
        slow = fast = head

        # Traverse the linked list with the fast and slow pointers.
        while fast != None and fast.next != None:
            slow = slow.next          # Move slow one step at a time.
            fast = fast.next.next    # Move fast two steps at a time.

            # If there is a cycle, the slow and fast pointers will eventually meet.
            if slow == fast:
                return True

        # If there is no cycle, the fast pointer will reach the end of the list.
        return False
