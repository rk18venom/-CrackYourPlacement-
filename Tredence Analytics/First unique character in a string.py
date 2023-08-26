#Problem Link: https://www.codingninjas.com/studio/problems/first-unique-character-in-a-string_982933?leftPanelTab=0

def firstUniqueCharacter(s, n):
    # Write your code here.
    dict1={}
    order=[]
    for x in s:
        if dict1.get(x,0)==0:
            order.append(x)
            dict1[x]=dict1.get(x,0)+1
        else:
            dict1[x]=dict1.get(x,0)+1
    ans=-1
    for y in order:
        if dict1.get(y,0)==1:
            ans=y
            break
    
    for i in range(n):
        if s[i]==ans:
            return i+1
    
    return -1