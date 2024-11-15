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

    def getSecondLargest2(self, arr):
        # Code Here
        prev=-1
        maxi=-1
        for x in arr:
            if maxi<x:
                prev=maxi
                maxi=x
            elif x!=maxi:
                prev=max(x,prev)
        return prev

    def getSecondLargest3(self, arr):
        first_largest, second_largest = -1, -1

        for i in arr:
            if i > first_largest:
                second_largest = first_largest
                first_largest = i
            elif i > second_largest and i < first_largest:
                second_largest = i
    
        return second_largest
                

#Main
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ob=Solution()
    print(ob.getSecondLargest(arr))

