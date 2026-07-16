# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values=[]
        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)
        inorder(root)
        for i in range(len(values)-1):
            if values[i+1]<=values[i]:
                return False
        return True