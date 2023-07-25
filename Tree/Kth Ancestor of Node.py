#Problem Link: https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1
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

def solution(root, res, node):
    if root is None:
        return False
    if root.data == node:
        return True
    if solution(root.left, res, node):
        res.append(root.data)
        return True
    elif solution(root.right, res, node):
        res.append(root.data)
        return True
    else:
        return False
        
def kthAncestor(root,k, node):
    #code here
    res=[]
    solution(root, res, node)
    if k-1 >= len(res):
        return -1
    return res[k-1]
        
k, node = map(int, input().split())
root=takeinput()
print("{}'th ancestor of {} is: {}".format(k, node, kthAncestor(root, k, node)))