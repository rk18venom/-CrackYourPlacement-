def sol(s):
    dict1={}
    order=[]
    for x in s:
        if dict1.get(x,0)==0:
            order.append(x)
        dict1[x]=dict1.get(x,0)+1
    ans=""
    for x in order:
        ans+=x
        ans+=str(dict1.get(x,0))
    return ans

s=input()
print(sol(s))