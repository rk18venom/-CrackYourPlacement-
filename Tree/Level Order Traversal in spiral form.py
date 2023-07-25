#Problem Link: https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1
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

def findSpiral(root):
    if root == None:
        return []
    q=[root]
    ans=[]
    level=0
    while len(q)>0 :
        size=len(q)
        temp=[]
        while size>0:
            curr=q.pop(0)
            temp.append(curr.data)
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
            size-=1
        
        if level%2==0:
            ans+=temp[::-1]
        else:
            ans+=temp
        level+=1
    return ans

root=takeinput()
print("Level order traversal in spiral form of Binary Tree: {}".format(findSpiral(root)))
        