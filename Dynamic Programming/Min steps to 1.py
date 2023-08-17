import sys
sys.setrecursionlimit(10**6)


def minStepsTo1(n, dp):
    if n==1 or n==0:
        return 0
    
    ans1=sys.maxsize
    ans2=sys.maxsize
    ans3=sys.maxsize

    if n%3==0:
        if dp[n//3]==-1:
            ans1=minStepsTo1(n//3,dp)
            dp[n//3]=ans1
        else:
            ans1=dp[n//3]
    elif n%2==0:
        if dp[n//2]==-1:
            ans2=minStepsTo1(n//2,dp)
            dp[n//2]=ans2
        else:
            ans2 = dp[n//2]
    else:
        if dp[n-1]==-1:
            ans3=minStepsTo1(n-1,dp)
            dp[n-1]=ans3
        else:
            ans3=dp[n-1]
    ans=1+min(ans1, ans2, ans3)
    return ans

n=int(input())
dp=[-1 for i in range(n+1)]
print(minStepsTo1(n,dp))

