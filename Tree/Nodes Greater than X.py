def countNodesGreaterThanX(root, X):
    if root is None:
        return 0
    leftCount=countNodesGreaterThanX(root.left, X)
    rightCount=countNodesGreaterThanX(root.right, X)
    if root.val>=X:
        return 1+leftCount+rightCount
    else:
        return leftCount+rightCount