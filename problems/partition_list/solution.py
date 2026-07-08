# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode(0)
        more=ListNode(0)
        lesstail=less
        moretail=more
        curr = head
        while curr:
            if curr.val<x:
                lesstail.next=curr
                lesstail=lesstail.next
            elif curr.val>=x:
                moretail.next=curr
                moretail=moretail.next
            curr=curr.next
        moretail.next=None
        lesstail.next=more.next
        return less.next