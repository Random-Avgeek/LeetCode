# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        slow=head
        curr=None
        fast=head
        while n-1>0:
            fast=fast.next
            n-=1
        while fast.next:
            fast=fast.next
            curr=slow
            slow=slow.next
        if slow == head:
            return head.next
        curr.next=slow.next
        return head