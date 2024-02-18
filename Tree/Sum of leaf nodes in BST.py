#Problem Link: https://www.geeksforgeeks.org/problems/sum-of-leaf-nodes-in-bst/1

'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def helper(self, root, ans):
        if root==None:
            return ans
        if root.left==None and root.right==None:
            ans+=root.data
            return ans
        
        return self.helper(root.left, ans) + self.helper(root.right, ans)
        
    def sumOfLeafNodes(self, root):
        #Your code here
        ans=0
        ans=self.helper(root,ans)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data=0):
        self.data=data
        self.left=None
        self.right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root

for _ in range(int(input())):
    root=None
    sizeOfArray=int(input())
    arr=[int(x) for x in input().strip().split()]
    for i in arr:
        root=newNode(root,i)
    ob = Solution()
    print(ob.sumOfLeafNodes(root))
# } Driver Code Ends