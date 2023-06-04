def numNodes(root):
    if root is None:
        return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return leftCount+rightCount+1