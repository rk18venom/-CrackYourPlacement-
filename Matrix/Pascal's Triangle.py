#Problem Link: https://www.naukri.com/code360/problems/pascal-s-triangle_1089580?leftPanelTabValue=PROBLEM

def printPascal(n:int):
    ans=[]
    curr=[]
    for i in range(n):
        prev=[]
        t=0
        for j in range(i+1):
            if j==i:
                prev.append(1)
            else:
                s=t+curr[j]
                prev.append(s)
                t=curr[j]

        ans.append(prev)
        curr=prev
    return ans

t=int(input())
for _ in range(t):
    n=int(input())
    ans=printPascal(n)
    print(ans)
