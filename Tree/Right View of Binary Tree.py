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

def rightView(root, level, res):
    if root is None:
        return None
    # If the current node's depth equals to `level`, append its value into result list.
    if len(res)==level:
        res.append(root.data)
    rightView(root.right, level+1, res)
    rightView(root.left, level+1, res)

root=takeinput()
res=[]
rightView(root, 0, res)
print("Right View of Binary Tree: {}".format(res))