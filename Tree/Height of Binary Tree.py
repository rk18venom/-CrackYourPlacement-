def height(root) :
    if root == None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    length = max(leftHeight,rightHeight)
    return 1 + length

