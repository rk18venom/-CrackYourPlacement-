#Problem Link: https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeinput():
    arr=[int(x) for x in input().split()]
    i=0
    q=Queue()
    root=Node(arr[i])
    q.put(root)
    while (i<len(arr)//2) and q.empty()!=True:
        it=q.get()
        if arr[2*i+1]!=-1:
            it.left=Node(arr[2*i+1])
            q.put(it.left)
        else:
            it.left=None
        
        if arr[2*i+2]!=-1:
            it.right=Node(arr[2*i+2])
            q.put(it.right)
        else:
            it.right=None
        i+=1
    return root

def LCA(root, n1, n2):
    #code here
    if not root:
        return None
    if root.data==n1 or root.data==n2:
        return root
    leftAns=LCA(root.left,n1,n2)
    rightAns=LCA(root.right,n1,n2)
    if leftAns!=None and rightAns!=None:
        return root
    elif leftAns!=None and rightAns==None:
        return leftAns
    elif rightAns!=None and leftAns==None:
        return rightAns
    else:
        return None

root=takeinput()    
n1, n2 = map(int, input().split())
print("The common ancestor of {} and {} is: {}".format(n1, n2, LCA(root, n1, n2).data))