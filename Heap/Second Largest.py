#Link: https://www.geeksforgeeks.org/problems/second-largest3735/1


#Solution

import heapq
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        s=set(arr)
        l=list(s)
        if len(l)>1:
            heapq.heapify(l)
            ans=heapq.nlargest(2,l)
            return min(ans)
        else:
            return -1
#Main
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ob=Solution()
    print(ob.getSecondLargest(arr))

