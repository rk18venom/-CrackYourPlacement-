#Problem Link: https://practice.geeksforgeeks.org/problems/make-matrix-beautiful-1587115620/1

def findMinOpeartion(matrix, n):
    # Code here
    maxSum=0
    row=[0]*n
    col=[0]*n
    for i in range(n):
        for j in range(n):
            row[i]+=matrix[i][j]
            maxSum=max(row[i], maxSum)
            col[j]+=matrix[i][j]
            maxSum=max(col[j], maxSum)
    
    ans=0
    for i in range(n):
        row[i]=maxSum-row[i]
        ans+=row[i]
    return ans
