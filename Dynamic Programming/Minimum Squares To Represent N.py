
# Recursive DP
import math, sys
def solve(n, dp):
    if n==0:
        return 0
    i=1
    root=int(math.sqrt(n))
    ans=sys.maxsize
    while i<=root:
        if dp[n-(i**2)]==-1:
            currans=1+solve(n-(i**2), dp)
            dp[n-(i**2)]=currans
        else:
            currans=dp[n-(i**2)]
        ans=min(currans, ans)
        i+=1
    return ans

# Iterative DP
def solveI(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    for i in range(1, n+1):
        ans=sys.maxsize
        root=int(math.sqrt(i))
        for j in range(1, root+1):
            currAns = 1 + dp[i-(j**2)]
            ans=min(ans, currAns)
        dp[i]=ans
    return dp[n]

n=int(input())
dp=[-1 for i in range(n+1)]
print(solve(n, dp))