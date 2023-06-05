import sys
class Solution:
    
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def minDiff(self,root, K):
        # code here
        if root is None:
            return sys.maxsize
        
        diff = abs(root.data-K)
        if root.data>=K:
            diff=min(diff, self.minDiff(root.left,K))
        else:
            diff=min(diff, self.minDiff(root.right,K))
        return diff
