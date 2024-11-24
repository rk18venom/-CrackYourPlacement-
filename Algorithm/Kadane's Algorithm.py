#Link: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

#Soultion

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        N=len(arr)
        maxsum=0
        currsum=0
        n=N
        for i in range(n):
            currsum=currsum+arr[i]
            if currsum>maxsum:
                maxsum=currsum
            if currsum<0:
                currsum=0
        max_=max(arr)
        if max_<0:
            return max_
        return maxsum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends