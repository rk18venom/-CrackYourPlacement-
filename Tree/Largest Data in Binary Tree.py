def largestData(root):
    if root is None:
        return -1
    leftLargest=largestData(root.left)
    rightLargest=largestData(root.right)
    largest=max(root.data, leftLargest, rightLargest)
    return largest