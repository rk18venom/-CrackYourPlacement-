#Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#Preorder = Root Left right
#Inorder = Left Root right

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder)==0 and len(inorder)==0:
            return None
        
        data=preorder[0]
        root=TreeNode(data)
        
        i=inorder.index(data)
        inorderls=inorder[0:i]
        preorderls=preorder[1:i+1]
        
        leftsubtree=self.buildTree(preorderls,inorderls)
        root.left=leftsubtree
        
        inorderrs=inorder[i+1:]
        preorderrs=preorder[i+1:]
        
        rightsubtree=self.buildTree(preorderrs, inorderrs)
        root.right=rightsubtree
        
        return root