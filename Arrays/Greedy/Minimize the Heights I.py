#Link: https://www.geeksforgeeks.org/problems/minimize-the-heights-i/1

#Solution

#User function Template for python3

import sys
class Solution:
    def getMinDiff(self, k, arr):
        # code here
        arr.sort()
        n=len(arr)
        maxEle=-sys.maxsize
        minEle=sys.maxsize
        res=arr[n-1]-arr[0]
        for i in range(1,n):
            maxEle=max(arr[i-1]+k,arr[n-1]-k)
            minEle=min(arr[i]-k,arr[0]+k)
            
            res=min(maxEle-minEle,res)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends

