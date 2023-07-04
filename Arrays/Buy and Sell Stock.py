def solution(arr, n):
    profit=0
    for i in range(0,n-1):
        if arr[i]<arr[i+1]:
            profit+=arr[i+1]-arr[i]
    return profit


n=int(input())
arr=[int(x) for x in input().split()]
print(solution(arr,n))