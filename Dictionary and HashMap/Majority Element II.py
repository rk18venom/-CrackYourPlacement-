#Link: https://www.geeksforgeeks.org/problems/majority-vote/1

#Solution

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        dict1={}
        for x in arr:
            dict1[x]=dict1.get(x,0)+1
        n=len(arr)
        m=n/3
        ans=[]
        for key in dict1:
            if dict1[key]>m:
                ans.append(key)
        ans.sort()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends