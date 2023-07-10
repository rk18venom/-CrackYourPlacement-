#Problem Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/990852671/


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        lh=self.minDepth(root.left)
        rh=self.minDepth(root.right)
        if lh==0 and rh!=0:
            return rh+1
        elif lh!=0 and rh==0:
            return lh+1
        else:
            return min(lh+1,rh+1)