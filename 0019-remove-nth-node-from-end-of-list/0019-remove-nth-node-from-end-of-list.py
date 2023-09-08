# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        l=[]
        while temp!=None:
           l.append(temp.val) 
           temp=temp.next
        l=l[::-1]
        l=l[0:n-1] + l[n:]
        l=l[::-1]

        new = None
        add = None
        next_node = None
        for i in l:
            if new is None:
               new=ListNode(i)
               add=new
            else:
               next_node = ListNode(i)
               new.next = next_node
               new = next_node
        return add  