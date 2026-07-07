# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr=slow
        prev=None
        while curr:
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        left=head
        right=prev
        while right:
            if right.val!=left.val:
                return False
            right=right.next
            left=left.next
        return True
