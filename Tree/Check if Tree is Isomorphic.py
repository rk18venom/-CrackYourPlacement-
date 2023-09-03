#Problem Link: https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        #code here.
        if root1 is None and root2 is None:
            return True
            
        if root1 is None or root2 is None:
            return False
        
        if root1.data!=root2.data:
            return False
        
        return (self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(root1.right, root2.right)) or (self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(root1.right, root2.left))