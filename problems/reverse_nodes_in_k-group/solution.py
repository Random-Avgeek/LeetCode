# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next=head
        prevtail=dummy
        while True:
            ender=prevtail
            for _ in range(k):
                ender = ender.next
                if ender is None:
                    break
            
            if ender is None:
                break
            
            nextstart=ender.next
            start=prevtail.next
            curr=start
            prev=None

            for _ in range(k):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp

            prevtail.next=prev
            start.next=curr
            prevtail=start
        return dummy.next