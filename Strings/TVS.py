def solve(matrix, n, m):
    rem=[]
    for j in range(m):
        for i in range(n-1):
            if matrix[i][j]>matrix[i+1][j]:
                rem.append(j)
                break
    print(rem)            
    ans=[]
    for i in range(n):
        curr=[]
        for j in range(m):
            if j not in rem:
                curr.append(matrix[i][j])
        ans.append(curr)
    return ans

n=int(input())
m=int(input())
matrix=[[x for x in input().split()] for i in range(n)]
ans=solve(matrix, n, m)
print(ans)


