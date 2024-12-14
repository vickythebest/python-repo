class TreeNode(object):
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        total = 0
        # only left node val to added when there is no node attached below
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total