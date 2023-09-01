#Problem Link: https://practice.geeksforgeeks.org/problems/leftmost-and-rightmost-nodes-of-binary-tree/1

def printCorner(root):
    
    # print corner data, no need to print new line
    # code here
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
        
        if len(temp)>1:
            print(temp[0], end=" ")
            print(temp[-1], end=" ")
        else:
            print(temp[0], end=" ")
        level+=1
        
    return ans
