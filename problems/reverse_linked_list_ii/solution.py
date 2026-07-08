# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next=head
        leftnode=dummy
        for _ in range(left-1):
            leftnode=leftnode.next

        tail=leftnode.next
        prev=None
        curr=leftnode.next

        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        leftnode.next=prev
        tail.next=curr

        return dummy.next
