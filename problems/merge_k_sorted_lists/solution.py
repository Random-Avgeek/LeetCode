# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,head in enumerate(lists):
            if head is not None:
                heapq.heappush(heap,(head.val,i,head))
        new=ListNode(0)
        curr=new

        while heap:
            val,i,node=heapq.heappop(heap)
            curr.next=node
            curr=curr.next

            if node.next is not None:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return new.next