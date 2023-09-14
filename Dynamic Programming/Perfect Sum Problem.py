def perfectSum(arr, n, sum):
    # code here
    dp=[[0]*(sum+1) for _ in range(n+1)]
    dp[0]=[1]+[0]*sum
    
    mod=10**9+7
    
    # recursive scheme
    for i in range(1,n+1):
        for j in range(sum+1):
            if j>=arr[i-1]:
                dp[i][j]=(dp[i-1][j]+dp[i-1][j-arr[i-1]])%mod
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][sum]