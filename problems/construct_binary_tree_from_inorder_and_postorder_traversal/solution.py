# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        rootval=postorder[-1]
        print(rootval)
        root=TreeNode(rootval)
        mididx=inorder.index(rootval)
        root.left=self.buildTree(inorder[:mididx],postorder[:mididx])
        root.right=self.buildTree(inorder[mididx+1:],postorder[mididx:-1])
        return root