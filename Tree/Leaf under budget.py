#Problem Link: https://practice.geeksforgeeks.org/problems/leaf-under-budget/1

def leafNode(root):
    if root == None:
        return []
    q=[root]
    ans=[]
    level=1
    while len(q)>0 :
        size=len(q)
        temp=[]
        while size>0:
            curr=q.pop(0)
            
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
            if curr.left==None and curr.right==None:
                temp.append(level)
            size-=1
        
        ans+=temp
        level+=1
    return ans
        

def getCount(self,root,n):
    #code here
    ans=leafNode(root)
    ans.sort()
    m=len(ans)
    cnt=0
    i=0
    while n>0 and i<m:
        if ans[i]<=n:
            n-=ans[i]
            cnt+=1
        else:
            n-=ans[i]
        i+=1
    return cnt
            