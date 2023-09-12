# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or has only one node, in which case there can be no cycle.
        if not head or not head.next:
            return None  # If there is no cycle, return None
        
        # Initialize two pointers: slow and fast
        slow = head
        fast = head

        # Find the meeting point of slow and fast pointers
        while fast and fast.next:
            slow = slow.next        # Move slow one step
            fast = fast.next.next  # Move fast two steps
            if slow == fast:
                break  # Meeting point found (cycle detected)

        # If there's no meeting point (no cycle), return None
        if slow != fast:
            return None

        # Reset slow pointer to head and move both pointers at the same speed until they meet at the cycle's start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Return the node where the cycle starts (or None if there's no cycle)
        return slow
