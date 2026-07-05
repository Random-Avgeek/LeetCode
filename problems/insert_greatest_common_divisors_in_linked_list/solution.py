# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        curr=head
        while curr and curr.next:
            newnode=ListNode(gcd(curr.val,curr.next.val),curr.next)
            curr.next=newnode
            curr=curr.next.next
        return head

