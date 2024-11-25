#Link: https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1

#Solution

#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
    def maxProduct(self,arr):
        # code here
        n = len(arr)
        maxProd = arr[0]
        minProd = arr[0]
        result = arr[0]

        for i in range(1, n):
            if arr[i] < 0:
                maxProd, minProd = minProd, maxProd

            maxProd = max(arr[i], maxProd * arr[i])
            minProd = min(arr[i], minProd * arr[i])

            result = max(result, maxProd)

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends