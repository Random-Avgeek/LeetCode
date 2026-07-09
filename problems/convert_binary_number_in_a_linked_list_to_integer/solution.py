# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        num=0
        while curr:
            num = num | curr.val
            num<<=1
            curr=curr.next
        num>>=1
        return num