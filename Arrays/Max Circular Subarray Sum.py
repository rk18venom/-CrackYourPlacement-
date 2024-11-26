#Link: https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1

#Solution
'''
Intuition
The goal is to find the maximum sum of a subarray in a circular array. There are two possible cases for the subarray that yields this maximum sum:

Non-Circular Case: The subarray does not wrap around the edges of the array. This can be solved using Kadane’s Algorithm, which is used to find the maximum subarray sum in linear arrays.
Circular Case: The subarray wraps around the edges of the array. This can be solved by subtracting the minimum subarray sum from the total sum of the array. Why? Because subtracting the minimum subarray sum leaves us with the sum of the elements outside that subarray, effectively wrapping around.
The final answer is the maximum of these two cases.
'''

import sys

def kadaneMax(arr):
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
    
def smallestSumSubarr(arr, n):
    # to store the minimum value that is ending
    # up to the current index
    min_ending_here = sys.maxsize
     
    # to store the minimum value encountered so far
    min_so_far = sys.maxsize
     
    # traverse the array elements
    for i in range(n):
        # if min_ending_here > 0, then it could not possibly
        # contribute to the minimum sum further
        if (min_ending_here > 0):
            min_ending_here = arr[i]
         
        # else add the value arr[i] to min_ending_here 
        else:
            min_ending_here += arr[i]
          
        # update min_so_far
        min_so_far = min(min_so_far, min_ending_here)
     
    # required smallest sum contiguous subarray value
    return min_so_far
    
    
def circularSubarraySum(arr):
    ##Your code here
    max_ = kadaneMax(arr)
    n=len(arr)
    min_ = smallestSumSubarr(arr, n)
    totalSum = sum(arr)
    return max(max_ , totalSum-min_)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends