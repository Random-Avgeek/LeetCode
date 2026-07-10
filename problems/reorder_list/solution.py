# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast=head
        slow=head
        stack=[]
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr=slow.next
        while curr:
            stack.append(curr)
            curr=curr.next
        curr=head
        while curr!=slow:
            temp=curr.next
            if len(stack)==0:
                curr=curr.next
                continue
            curr.next=stack[-1]
            stack.pop()
            curr.next.next=temp
            curr=temp
        curr.next = None