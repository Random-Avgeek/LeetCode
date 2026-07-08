# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr is not None:
            if curr.left is not None:
                nxt=curr.left
                while nxt.right is not None:
                    nxt=nxt.right
                nxt.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right