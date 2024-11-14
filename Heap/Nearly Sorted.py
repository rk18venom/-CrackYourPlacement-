#Link: https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1

#Solution 

#Using Heapq

import heapq
class Solution:
    def nearlySorted(self, arr, k):
        #code
        a=arr
        n=len(a)
        ans=[-1]*n
        heapq.heapify(a)
        for i in range(n):
            ans[i]=heapq.heappop(a)
    
        for i in range(n):
            arr.append(ans[i])
         
        return arr

#Main
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    obj=Solution()
    print(*obj.nearlySorted(arr,k))


