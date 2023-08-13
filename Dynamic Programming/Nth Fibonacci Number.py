#Problem Link: https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1


def nthFibonacci(n):
    # code here
    M=10**9+7
    dp=[0]*(n+1)
    dp[1]=1
    if n==1:
        return dp[n]
    i=2
    while i<=n:
        dp[i]=(dp[i-1]+dp[i-2])%M
        i+=1
    return dp[n]%M

n=int(input())
print(nthFibonacci(n))
