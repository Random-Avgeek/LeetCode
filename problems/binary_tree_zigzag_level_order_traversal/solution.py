# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        res=[]
        count=1
        while queue:
            curr_level=[]
            level_size=len(queue)
            for i in range(level_size):
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                curr_level.append(curr.val)
            if count%2!=0:
                res.append(curr_level)
            else:
                res.append(curr_level[::-1])
            count+=1
        return res
            