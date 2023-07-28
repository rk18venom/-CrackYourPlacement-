#Problem Link: https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1?page=4&sortBy=submissions

def rowWithMax1s(arr, n, m):
    # code here
    ans=None
    max1=-1
    for i in range(n):
        prev=max1
        max1=max(sum(arr[i]), max1)
        if max1==sum(arr[i]) and max1!=prev:
            ans=i
    if max1==0:
        return -1
    return ans
        
tc = int(input())
while tc > 0:
    n, m = list(map(int, input().strip().split()))
    
    inputLine = list(map(int, input().strip().split()))
    arr = [[0 for j in range(m)] for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            arr[i][j] = inputLine[i * m + j]
    ans = rowWithMax1s(arr, n, m)
    print(ans)
    tc -= 1