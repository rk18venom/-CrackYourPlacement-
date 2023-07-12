#Problem Link: https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1

M=10**9+7

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        if R==0:
            return 1
        
        if R%2==0:
            ans=self.power(N,R//2)
            return (ans**2)%M
        else:
            ans=self.power(N,R//2)
            return ((ans**2)*N)%M
            
n, r = map(int, input().split())
obj = Solution()
print((obj.power(n,r)) % M )
