#Link: https://www.geeksforgeeks.org/problems/swap-and-maximize5859/1

#Solution

def maxSum(arr):
    # code here
    arr.sort()
    l=[]
    n=len(arr)
    i=0
    j=n-1
    while i<j:
        if i<n:
            l.append(arr[i])
            i+=1
        if j>0:
            l.append(arr[j])
            j-=1
    if n%2!=0:
        l.append(arr[i])
    #print(l)
    ans=0
    for i in range(n-1):
        ans+=abs(l[i]-l[i+1])
    ans+=abs(l[-1]-l[0])
    return ans

#Main
t=int(input())
while t!=0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxSum(arr))
    t-=1
