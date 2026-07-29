# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot and not root:
            return True
        if not subRoot and root:
            return False
        if not root and subRoot:
            return False

        if root.val == subRoot.val and self.sameTree(root, subRoot):
            return True
        
        else:
            if root.left and self.isSubtree(root.left, subRoot):
                return True
            if root.right and self.isSubtree(root.right, subRoot):
                return True
        

        return False

    def sameTree(self, root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root and not root2:
            return True
        
        if (not root and root2) or (not root2 and root):
            return False
        
        return root.val == root2.val and self.sameTree(root.left, root2.left) and self.sameTree(root.right, root2.right)
        