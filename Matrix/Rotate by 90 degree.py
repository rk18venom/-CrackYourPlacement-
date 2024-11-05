#Link: https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/1

#Solution:

def rotate(mat): 
    #code here
    n=len(mat)
    m=len(mat[0])
    for i in range(n):
        for j in range(i+1,m):
            temp=mat[i][j]
            mat[i][j]=mat[j][i]
            mat[j][i]=temp
            
    for i in range(n):
        mat[i]=mat[i][::-1]
    
    return mat
            




t = int(input())
for _ in range(t):
    N = int(input())
    matrix = []
    for i in range(N):
        arr = [int(x) for x in input().strip().split()]
        matrix.append(arr)

    rotate(matrix)
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()