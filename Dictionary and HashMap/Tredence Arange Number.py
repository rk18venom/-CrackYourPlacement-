def solve(n, p):
    p.sort()
    dict1={}
    order=[]
    ans=[]
    for i in range(n):
        x, y=p[i][0], p[i][1]
        if dict1.get(x,0)==0:
            curr=[]
            curr.append(p[i])
            dict1[x]=curr
            order.append(x)
        else:
            curr=dict1[x]
            curr.append(p[i])
    
    ans=[]
    for z in order:
        curr=dict1[z]
        curr=sorted(curr, key=lambda x:x[1], reverse=True)
        ans+=curr
    return ans     

   