# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(0)
        temp.next=head
        curr = temp

        while curr.next and curr.next.next:
            first=curr.next
            second=curr.next.next

            first.next=second.next
            second.next=first
            curr.next=second

            curr=first
        return temp.next