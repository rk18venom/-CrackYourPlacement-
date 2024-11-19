#Link: https://www.geeksforgeeks.org/problems/next-permutation5226/1

#Solution

#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        pivot=None
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot=i
                break
        if pivot ==None:
            arr.reverse()
            return arr
        succ=-1
        for i in range(n-1,-1,-1):
            if arr[pivot]<arr[i]:
                succ=i
                break
        temp=arr[pivot]
        arr[pivot]=arr[succ]
        arr[succ]=temp
        arr[pivot+1:]=arr[pivot+1:][::-1]
        return arr
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends