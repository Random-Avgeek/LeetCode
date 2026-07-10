# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revlist(self,head):
        prev=None
        while head:
            nxt=head.next
            head.next=prev
            prev=head
            head=nxt
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1=self.revlist(l1)
        r2=self.revlist(l2)
        head = None
        carry = 0
        while r1 or r2 or carry:
            val1=r1.val if r1 else 0
            val2=r2.val if r2 else 0
            total = val1+val2+carry
            carry=total//10
            newnode=ListNode(total%10)
            newnode.next=head
            head=newnode
            if r1:
                r1=r1.next
            if r2:
                r2=r2.next
        return head
        
