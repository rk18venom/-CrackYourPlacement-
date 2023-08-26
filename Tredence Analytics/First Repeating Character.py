#Problem Link: https://www.codingninjas.com/studio/problems/first-repeated-character_1214646?leftPanelTab=1

def repeatedCharacter(s):
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
        if dict1.get(y,0)>1:
            ans=y
            break
    
    return ans