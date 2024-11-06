#Link: https://leetcode.com/problems/custom-sort-string/description/

#Solution
def customSortString(y: str, x: str):
    lx=list(x)
    ly=list(y)
    m=len(lx)
    n=len(ly)
    dict1={}
    for i in range(m):
        dict1[lx[i]]=dict1.get(lx[i],0)+1
    s=""
    for i in range(n):
        if dict1.get(ly[i],0)!=0:
            t=dict1[ly[i]]
            for j in range(t):
                s+=ly[i]
            dict1[ly[i]]=0
    s1=''
    for key in dict1:
        if dict1[key]!=0:
            for j in range(dict1[key]):
                s1+=key

    lx=s1+s
    return lx

#input
t=int(input())
while t!=0:
    y=input()
    x=input()
    print(customSortString(y, x))
    t=t-1