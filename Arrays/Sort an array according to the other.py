#Problem Link: https://practice.geeksforgeeks.org/problems/relative-sorting4323/1?page=2&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

def relativeSort (A1, N, A2, M):
    # Your Code Here
    dict1={}
    order=[]
    for x in A2:
        if dict1.get(x,0)==0:
            dict1[x]=1
            order.append(x)
    
    A1.sort()
    dict2={}
    rem=[]
    for x in A1:
        if dict1.get(x,0)==1:
            dict2[x]=dict2.get(x,0)+1
        else:
            rem.append(x)
    
    ans=[]
    for x in order:
        curr=[]
        if dict2.get(x,0)!=0:
            curr=[x]*dict2[x]
        ans+=curr
    ans+=rem
    return ans