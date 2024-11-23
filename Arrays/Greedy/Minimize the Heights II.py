#Link: https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1

#Solution

#User function Template for python3
import sys
class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        n=len(arr)
        maxEle=-sys.maxsize
        minEle=sys.maxsize
        res=arr[n-1]-arr[0]
        for i in range(1,n):
            if arr[i]>=k:
                maxEle=max(arr[i-1]+k, arr[n-1]-k)
                minEle=min(arr[i]-k, arr[0]+k)
                res=min(maxEle-minEle, res)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends