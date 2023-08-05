#Problem Link: https://leetcode.com/problems/rotate-image/

#Step 1: First Transpose
#Step 2: Then reverse each row 

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(m):
        matrix[i]=matrix[i][::-1]

m=int(input())
n=int(input())
matrix=[[int(x) for x in input().split()] for i in range(m)]
rotate(matrix)
for i in range(m):
    print(matrix[i])
