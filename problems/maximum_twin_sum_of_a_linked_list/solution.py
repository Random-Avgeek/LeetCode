# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        prev=None
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev = curr
            curr=nextnode

        left=head
        right=prev
        max_sum=0

        while right:
            currsum=left.val+right.val
            max_sum=max(max_sum,currsum)
            left=left.next
            right=right.next
        
        return max_sum