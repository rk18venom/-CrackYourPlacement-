#Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

# A class to store a binary tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Traverse the tree in a preorder fashion and store nodes in a dictionary
# corresponding to their level
def preorder(root, level, d):
 
    # base case: empty tree
    if root is None:
        return
 
    # insert the current node and its level into the dictionary
    d.setdefault(level, []).append(root.key)
 
    # recur for the left and right subtree by increasing the level by 1
    preorder(root.left, level + 1, d)
    preorder(root.right, level + 1, d)
 
 
# Recursive function to print level order traversal of a given binary tree
def levelOrderTraversal(root):
 
    # create an empty dictionary to store nodes between given levels
    d = {}
 
    # traverse the tree and insert its nodes into the dictionary
    # corresponding to their level
    preorder(root, 1, d)
 
    # iterate through the dictionary and print all nodes between given levels
    for i in range(1, len(d) + 1):
        print(f'Level {i}:', d[i])
 
 
if __name__ == '__main__':
 
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    root.right.right.right = Node(30)
 
    levelOrderTraversal(root)
 

'''
Output:

Level 1: [15]
Level 2: [10, 20]
Level 3: [8, 12, 16, 25]
Level 4: [30]

'''