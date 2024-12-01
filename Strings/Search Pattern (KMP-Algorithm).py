#Link: https://www.geeksforgeeks.org/problems/search-pattern0205/1

#Solution

#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        l=len(pat)
        ans=[]
        n=len(txt)
        for i in range(n-l+1):
            curr=txt[i:l+i]
            #print(curr, pat)
            if curr==pat:
                ans.append(i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends