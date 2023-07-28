#Problem Link: https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?page=3&sortBy=submissions


def find3Numbers(A, n, y):
        # Your Code Here
        A.sort()
        for i in range(n):
            y = X - A[i]
            low = i+1
            high = n-1
            while(low < high):
                if A[low] + A[high] == y:
                    return 1
                elif A[low] + A[high] > y:
                    high -= 1
                else:
                    low += 12
        
        return 0


t=int(input())
for _ in range(t):
     N ,X=[int(x) for x in input().split()]
     arr=[]
     for j in range (N):
        a_j= int(input())
        arr.append(a_j)
     print("YES" if find3Numbers(arr, N, X)==1 else "No")