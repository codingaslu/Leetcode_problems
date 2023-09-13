#link-https://www.youtube.com/watch?v=-NhA6WDEcy4
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list of length k
        def reverse(head, k):
            prev = None
            cur = head
            for i in range(k):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return prev
        
        # Check if there are at least k nodes remaining to reverse
        count = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count += 1
        
        if count < k:
            return head  # Not enough nodes to reverse
        
        # Reverse the first k nodes and connect them to the remaining list
        new_head = reverse(head, k)
        head.next = self.reverseKGroup(cur, k)
        
        return new_head
