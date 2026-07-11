# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None for _ in range(k)]
        curr=head
        size=0
        while curr:
            curr=curr.next
            size+=1
        listsize=size//k
        extralists=size%k
        heads=[ListNode(0) for _ in range(k)]
        tails=[node for node in heads]
        curr=head
        n=0
        i=0

        targetsize = listsize
        if extralists > 0:
            targetsize = listsize + 1
        
        while curr:
            nextnode=curr.next
            curr.next=None
            tails[i].next=curr
            tails[i]=tails[i].next
            n+=1
            if n>=targetsize:
                i+=1
                n=0

                if extralists>0:
                    extralists-=1
                
                if extralists > 0:
                    targetsize = listsize + 1
                else:
                    targetsize = listsize

            curr=nextnode
        for i in range(len(heads)):
            heads[i]=heads[i].next
        return heads