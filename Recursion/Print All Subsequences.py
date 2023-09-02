def printAllSubsequences(arr, n, i, curr):
    if i>=n:
        print(curr)
        return 
    curr.append(arr[i])
    printAllSubsequences(arr, n, i+1, curr)
    curr.pop()
    printAllSubsequences(arr, n, i+1, curr)

n=int(input())
arr=[int(x) for x in input().split()]
printAllSubsequences(arr, n, 0, [])