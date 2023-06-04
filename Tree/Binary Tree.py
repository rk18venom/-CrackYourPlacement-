class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData=int(input())
    if rootData == -1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree =takeInput()
    rightTree = takeInput()
    root.left=leftTree
    root.right=rightTree
    return root



def printTree(root):
    if root is None:
        return None
    print(root.data, end=":")
    if root.left is not None:
        print("L",root.left.data, end=",")
    if root.right is not None:
        print("R",root.right.data, end="")
    print()
    printTree(root.left)
    printTree(root.right)


root=takeInput()
printTree(root)