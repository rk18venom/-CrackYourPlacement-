#Problem Link: https://leetcode.com/problems/rotate-image/

#Step 1: First Transpose
#Step 2: Then rverse each row 

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    dict1={}
    m=len(matrix)
    n=len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if (i,j) not in dict1 or (j,i) not in dict1:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                dict1[(i,j)]=1
                dict1[(j,i)]=1
    
    for i in range(m):
        matrix[i]=matrix[i][::-1]
    